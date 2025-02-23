__all__ = ("AuthMixin", "UserMixin", "DatabaseMixin",
           "StorageMixin", "FirestoreMixin", "PhoneMixin")

from sjfirebase.jinterface.task import OnCompleteListener
from sjfirebase.jinterface.firestore import EventListener
from sjfirebase.jinterface.database import ValueEventListener
from sjfirebase.jinterface.phone import VerificationStateChangeCallback
from jnius import autoclass

from sjfirebase.tools import is_jnull
from sjfirebase.tools.serializer import serialize
from android.activity import _activity  # noqa
from sjfirebase.jclass.firestore import Source


class __Firebase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self, AuthMixin):
            from sjfirebase.jclass.emailauth import SJFirebaseAuthEmail
            self.auth = SJFirebaseAuthEmail
        if isinstance(self, UserMixin):
            from sjfirebase.jclass.user import SJFirebaseUser
            self.user = SJFirebaseUser
        if isinstance(self, DatabaseMixin):
            from sjfirebase.jclass.database import SJFirebaseDatabase
            self.database = SJFirebaseDatabase
        if isinstance(self, StorageMixin):
            from sjfirebase.jclass.storage import SJFirebaseStorage
            self.storage = SJFirebaseStorage
        if isinstance(self, FirestoreMixin):
            from sjfirebase.jclass.firestore import SJFirebaseFirestore
            self.firestore = SJFirebaseFirestore
        if isinstance(self, PhoneMixin):
            from sjfirebase.jclass.phoneauth import SJFirebaseAuthPhone
            self.phone = SJFirebaseAuthPhone


class __BaseMixin(__Firebase):
    listener = None
    listener_registration = {}
    _ = None

    @staticmethod
    def on_complete_listener(callback):
        return OnCompleteListener(callback)

    @staticmethod
    def event_listener(callback):
        return EventListener(callback)

    @staticmethod
    def value_event_listener(callback):
        return ValueEventListener(callback, lambda _: None)

    def gc_listener(self):
        self.listener = None

    def detach_all_snapshot_listener(self):
        if not self.listener_registration:
            return
        if isinstance(self.listener_registration, dict):
            for key, registration in self.listener_registration.items():
                if not registration:
                    continue
                registration.remove()
                self.listener_registration[key] = None
                return
        self.gc_listener()

    def detach_snapshot_listener(self, document_or_collection_path):
        self.listener_registration[document_or_collection_path].remove()
        self.listener_registration[document_or_collection_path] = None


class AuthMixin(__BaseMixin):
    auth_listener = None

    def get_auth(self):
        return self.auth.get_instance()

    def create_user_with_email_and_password(self, email, password, listener):
        self.auth_listener = self.on_complete_listener(listener)
        auth = self.get_auth()
        (
            auth
            .createUserWithEmailAndPassword(email, password)
            .addOnCompleteListener(self.auth_listener)
        )

    def sign_in_with_email_and_password(self, email, password, listener):
        self.auth_listener = self.on_complete_listener(listener)
        auth = self.get_auth()
        (
            auth
            .signInWithEmailAndPassword(email, password)
            .addOnCompleteListener(self.auth_listener)
        )

    def sing_in_with_credential(self, credential, listener):
        self.auth_listener = self.on_complete_listener(listener)
        auth = self.get_auth()
        (
            auth
            .signInWithCredentials(credential)
            .addOnCompleteListener(self.auth_listener)
        )

    def logout(self):
        self.get_auth().signOut()


class UserMixin(__BaseMixin):
    def get_current_user(self):
        user = self.user.get_current_user()
        if user:
            user.reload()
        return user

    @property
    def is_email_verified(self):
        user = self.get_current_user()
        return user.isEmailVerified()

    def send_email_verification(self):
        user = self.get_current_user()
        user.sendEmailVerification()

    def set_display_name(self, name):
        req = self.user.profile_change_request_builder()
        req.setDisplayName(name)
        req = req.build()
        self.update_profile(req)

    def get_uid(self):
        user = self.get_current_user()
        return user.getUid()

    def get_email(self):
        user = self.get_current_user()
        return user.getEmail()

    def get_display_name(self):
        user = self.get_current_user()
        return user.getDisplayName()

    def get_details(self):
        return dict(
            email=self.get_email(),
            name=self.get_display_name()
        )

    def update_profile(self, profile_update):
        user = self.get_current_user()
        user.updateProfile(profile_update)


class FirestoreMixin(__BaseMixin):
    firestore_listeners = []
    last_visible = {}

    def __construct_set_callback__(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    None if task.isSuccessful()
                    else task.getException().toString()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_get_document_callback__(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    serialize(task.getResult().getData())
                    | {"document_id": task.getResult().getId()}
                    if task.isSuccessful()
                    else task.getException().toString()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_get_collection_callback__(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    [
                        serialize(document.getData())
                        | {"document_id": document.getId()}
                        for document in task.getResult()
                    ] if task.isSuccessful()
                    else task.getException().toString()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_document_snapshot_callback__(self, listener):
        callback = self.event_listener(
            lambda snapshot, error:
                listener(
                    error.toString() if not is_jnull(error)
                    else serialize(snapshot.getData()) | {"document_id": snapshot.getId()}
                    if not is_jnull(snapshot) and snapshot.exists()
                    else None,
                    "Local" if not is_jnull(snapshot) and snapshot.getMetadata().hasPendingWrites()
                    else "Server"
                )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_collection_snapshot_callback__(self, listener, listen_for_changes):
        Type = autoclass("com.google.firebase.firestore.DocumentChange$Type")
        callback = self.event_listener(
            lambda snapshot, error:
                listener(
                    error.toString() if not is_jnull(error)
                    else [
                        serialize(document.getDocument().getData()) | {
                            "document_id": document.getDocument().getId(),
                            "document_type":
                                "ADDED" if document.getType().ordinal() == Type.ADDED.ordinal() else
                                "MODIFIED" if document.getType().ordinal() == Type.MODIFIED.ordinal() else
                                "REMOVED"
                        }
                        for document in snapshot.getDocumentChanges()
                    ] if listen_for_changes else [
                        serialize(document.getData()) | {"document_id": document.getId()}
                        for document in snapshot
                    ],
                    "Local" if not is_jnull(snapshot) and snapshot.getMetadata().hasPendingWrites()
                    else "Server"
                )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_pagination_of_document_callback__(self, listener, collection_path):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    [
                        serialize(document.getData())
                        | {"document_id": document.getId()}
                        for document in task.getResult()
                    ] if task.isSuccessful()
                    else task.getException().toString()
                ),
                self.firestore_listeners.remove(callback),
                self.last_visible.update(
                    {
                        collection_path:
                            task.getResult().getDocuments().get(
                                task.getResult().size() - 1
                            )
                    }
                ),
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    @staticmethod
    def __set_source__(source):
        match source:
            case "default":
                source = Source.DEFAULT
            case "server":
                source = Source.SERVER
            case "cache":
                source = Source.CACHE
            case None:
                pass
            case _:
                raise Exception("source must be 'default' or 'server' or 'cache'")
        return source

    def collection(self, path):
        db = self.firestore.get_db()
        return db.collection(path)

    def document(self, path):
        db = self.firestore.get_db()
        return db.document(path)

    def add_document(self, collection_path, data, listener):
        (
            self.collection(collection_path)
            .add(serialize(data))
            .addOnCompleteListener(self.__construct_set_callback__(listener))
        )

    def set_document(self, document_path, data, listener, merge=False):
        if merge:
            SetOptions = autoclass("com.google.firebase.firestore.SetOptions")
            (
                self.document(document_path)
                .set(serialize(data), SetOptions.merge())
                .addOnCompleteListener(self.__construct_set_callback__(listener))
            )
        else:
            (
                self.document(document_path)
                .set(serialize(data))
                .addOnCompleteListener(self.__construct_set_callback__(listener))
            )

    def update_document(self, document_path, data, listener):
        (
            self.document(document_path)
            .update(*serialize(data, True))
            .addOnCompleteListener(self.__construct_set_callback__(listener))
        )

    def delete_document(self, document_path, listener):
        (
            self.document(document_path)
            .delete()
            .addOnCompleteListener(self.__construct_set_callback__(listener))
        )

    def get_document(self, document_path, listener, source=None):
        source = self.__set_source__(source)
        document = self.document(document_path)
        if source:
            document = document.get(source)
        else:
            document = document.get()
        document.addOnCompleteListener(self.__construct_get_document_callback__(listener))

    def get_collection_of_documents(self, collection_path, listener, source=None):
        source = self.__set_source__(source)
        collection = self.collection(collection_path)
        if source:
            collection = collection.get(source)
        else:
            collection = collection.get()
        collection.addOnCompleteListener(self.__construct_get_collection_callback__(listener))

    def add_document_snapshot_listener(self, document_path, listener):
        callback = self.__construct_document_snapshot_callback__(listener)
        (
            self.document(document_path)
            .addSnapshotListener(callback)
        )
        self.listener_registration[document_path] = callback

    def add_collection_snapshot_listener(self, collection_path, listener, listen_for_changes=True):
        callback = self.__construct_collection_snapshot_callback__(listener, listen_for_changes)
        (
            self.collection(collection_path)
            .addSnapshotListener(callback)
        )
        self.listener_registration[collection_path] = callback

    def get_pagination_of_documents(self, collection_path, limit, listener, source=None):
        source = self.__set_source__(source)
        collection = self.collection(collection_path)
        if last_visible := self.last_visible.get(collection_path):
            collection = collection.startAfter(last_visible)
        collection = collection.limit(limit)
        if source:
            collection = collection.get(source)
        else:
            collection = collection.get()
        collection.addOnCompleteListener(
            self.__construct_pagination_of_document_callback__(listener, collection_path))


class DatabaseMixin(__BaseMixin):
    def get_db_reference(self, path=None):
        db = self.database.get_db()
        if path:
            return db.getReference(path)
        return db.getReference()


class StorageMixin(__BaseMixin):
    def get_storage_reference(self, path=None):
        storage = self.storage.get_instance()
        if path:
            return storage.getReference(path)
        return storage.getReference()


class PhoneMixin(__BaseMixin):
    _callback = None
    _state_change = None

    def __init__(self, on_code_sent, on_verification_completed, on_verification_failed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._callback = VerificationStateChangeCallback(
            on_code_sent,
            on_verification_completed,
            lambda e: on_verification_failed(e.toString())
        )
        self._state_change = autoclass("com.simplejnius.sjfirebase.callback.VerificationStateChange")()
        self._state_change.setCallback(self._callback)

    @staticmethod
    def _long(num):
        return autoclass("java.lang.Long")(num)

    def start_phone_number_verification(self, phone_number, timeout):
        self.phone.startPhoneNumberVerification(
            phone_number,
            self._long(timeout),
            _activity,
            self._state_change
        )

    def resend_verification_code(self, phone_number, timeout, token):
        self.phone.resendVerificationCode(
            phone_number,
            self._long(timeout),
            _activity,
            self._state_change,
            token
        )
