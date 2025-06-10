__all__ = ("AuthMixin", "UserMixin", "DatabaseMixin",
           "StorageMixin", "FirestoreMixin", "PhoneMixin",
           "FunctionMixin")

from itertools import chain
from typing import Callable
from sjfirebase.jclass.emailauth import EmailAuthProvider
from sjfirebase.jclass.transaction import Transaction
from sjfirebase.jinterface.task import OnCompleteListener, Continuation
from sjfirebase.jinterface.firestore import EventListener
from sjfirebase.jinterface.database import ValueEventListener, CompletionListener, TransactionHandler
from sjfirebase.jinterface.phone import VerificationStateChangeCallback
from jnius import autoclass, cast, JavaException

from sjfirebase.tools import is_jnull, uri_parse
from sjfirebase.tools.serializer import serialize
from android.activity import _activity  # noqa
from sjfirebase.jclass.firestore import Source


class __Firebase:
    instance = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self, AuthMixin):
            from sjfirebase.jclass.emailauth import SJFirebaseAuthEmail
            self.auth = SJFirebaseAuthEmail
            self.instance = self.auth.get_instance()
        if isinstance(self, UserMixin):
            from sjfirebase.jclass.user import SJFirebaseUser
            self.user = SJFirebaseUser
        if isinstance(self, DatabaseMixin):
            from sjfirebase.jclass.database import SJFirebaseDatabase
            self.database = SJFirebaseDatabase
            self.instance = self.database.get_db()
        if isinstance(self, StorageMixin):
            from sjfirebase.jclass.storage import SJFirebaseStorage
            self.storage = SJFirebaseStorage
            self.instance = self.storage.get_instance()
        if isinstance(self, FirestoreMixin):
            from sjfirebase.jclass.firestore import SJFirebaseFirestore
            self.firestore = SJFirebaseFirestore
            self.instance = self.firestore.get_db()
        if isinstance(self, PhoneMixin):
            from sjfirebase.jclass.phoneauth import SJFirebaseAuthPhone
            self.phone = SJFirebaseAuthPhone
            self.instance = self.phone.get_instance()
        if isinstance(self, FunctionMixin):
            from sjfirebase.jclass.function import FirebaseFunctions
            self.functions = FirebaseFunctions
            self.instance = self.functions.getInstance()


class __BaseMixin(__Firebase):
    listener = None
    listener_registration = {}
    value_event_listeners = {}
    _ = None

    def use_emulator(self, host: str, port: int):
        self.instance.useEmulator(host, port)

    @staticmethod
    def on_complete_listener(callback):
        return OnCompleteListener(callback)

    @staticmethod
    def event_listener(callback):
        return EventListener(callback)

    @staticmethod
    def completion_listener(callback):
        return CompletionListener(callback)

    @staticmethod
    def value_event_listener(on_data_changed, on_cancelled=lambda _: None):
        return ValueEventListener(on_data_changed, on_cancelled)

    @staticmethod
    def transaction_handler(do_transaction, on_complete):
        return TransactionHandler(do_transaction, on_complete)

    @staticmethod
    def continuation(callback):
        return Continuation(callback)

    def gc_listener(self):
        self.listener = None

    def detach_all_snapshot_listener(self):
        if not self.listener_registration:
            return
        if isinstance(self.listener_registration, dict):
            for key, registration in self.listener_registration.items():
                if not registration:
                    continue
                registration[1].remove()
                self.listener_registration[key] = None
            return
        self.gc_listener()

    def detach_snapshot_listener(self, document_or_collection_path):
        self.listener_registration[document_or_collection_path][1].remove()
        self.listener_registration[document_or_collection_path] = None

    def remove_all_value_event_listener(self):
        if not self.value_event_listeners:
            return
        if isinstance(self.value_event_listeners, dict):
            for key, event_listener in self.value_event_listeners.items():
                if not event_listener:
                    continue
                event_listener[1].removeEventListener()
                self.value_event_listeners[key] = None
            return
        self.gc_listener()

    def remove_value_event_listener(self, path):
        self.value_event_listeners[path][1].removeEventListener()
        self.value_event_listeners[path] = None


class AuthMixin(__BaseMixin):
    auth_listener = None

    def __construct_auth_callback(self, listener):
        callback = self.on_complete_listener(
            lambda task: (
                listener(
                    task.isSuccessful(),
                    None if task.isSuccessful()
                    else task.getException().getMessage()
                ),
                setattr(self, "auth_listener", None)
            )
        )
        return callback

    def get_auth(self):
        return self.auth.get_instance()

    def create_user_with_email_and_password(self, email, password, listener):
        self.auth_listener = self.__construct_auth_callback(listener)
        auth = self.get_auth()
        (
            auth
            .createUserWithEmailAndPassword(email, password)
            .addOnCompleteListener(self.auth_listener)
        )

    def sign_in_with_email_and_password(self, email, password, listener):
        self.auth_listener = self.__construct_auth_callback(listener)
        auth = self.get_auth()
        (
            auth
            .signInWithEmailAndPassword(email, password)
            .addOnCompleteListener(self.auth_listener)
        )

    def sign_in_with_credential(self, credential, listener):
        self.auth_listener = self.__construct_auth_callback(listener)
        auth = self.get_auth()
        (
            auth
            .signInWithCredential(credential)
            .addOnCompleteListener(self.auth_listener)
        )

    @staticmethod
    def get_email_auth_provider_credential(email, password):
        return EmailAuthProvider.getCredential(email, password)

    def logout(self):
        self.get_auth().signOut()


class UserMixin(__BaseMixin):
    email_update_listener = None
    profile_update_listener = None
    password_update_listener = None
    email_verification_listener = None
    password_reset_listener = None
    user_delete_listener = None
    link_credential_listener = None
    user_reauthenticate_listener = None

    def __construct_user_callback(self, listener, listener_name):
        callback = self.on_complete_listener(
            lambda task: (
                listener(
                    task.isSuccessful(),
                    None if task.isSuccessful()
                    else task.getException().getMessage()
                ),
                setattr(self, listener_name, None)
            )
        )
        return callback

    def get_current_user(self):
        user = self.user.get_current_user()
        if user:
            user.reload()
        return user

    @property
    def is_email_verified(self):
        user = self.get_current_user()
        return user.isEmailVerified()

    def send_email_verification(self, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.sendEmailVerification()
        self.email_verification_listener = self.__construct_user_callback(
            listener, "email_verification_listener")
        task.addOnCompleteListener(self.email_verification_listener)

    def send_password_reset_email(self, email, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.sendPasswordResetEmail(email)
        self.password_reset_listener = self.__construct_user_callback(
            listener, "password_reset_listener")
        task.addOnCompleteListener(self.password_reset_listener)

    def get_uid(self):
        user = self.get_current_user()
        return user.getUid()

    def get_email(self):
        user = self.get_current_user()
        return user.getEmail()

    def get_phone_number(self):
        user = self.get_current_user()
        return user.getPhoneNumber()

    def get_display_name(self):
        user = self.get_current_user()
        return user.getDisplayName()

    def get_details(self):
        return dict(
            email=self.get_email(),
            name=self.get_display_name()
        )

    def update_profile(self, display_name=None, photo_url=None, listener=lambda *_: None):
        user = self.get_current_user()
        profile_update = self.user.profile_change_request_builder()
        if not (display_name or photo_url):
            return
        if display_name:
            profile_update.setDisplayName(display_name)
        if photo_url:
            profile_update.setPhotoUri(uri_parse(photo_url))
        profile_update = profile_update.build()
        task = user.updateProfile(profile_update)
        self.profile_update_listener = self.__construct_user_callback(
            listener, "profile_update_listener")
        task.addOnCompleteListener(self.profile_update_listener)

    def update_email(self, email, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.updateEmail(email)
        self.email_update_listener = self.__construct_user_callback(
            listener, "email_update_listener")
        task.addOnCompleteListener(self.email_update_listener)

    def update_password(self, password, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.updatePassword(password)
        self.password_update_listener = self.__construct_user_callback(
            listener, "password_update_listener")
        task.addOnCompleteListener(self.password_update_listener)

    def link_with_credential(self, credential, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.linkWithCredential(credential)
        self.link_credential_listener = self.__construct_user_callback(
            lambda suc, err: (
                AuthMixin().sign_in_with_credential(credential, listener)
                if suc else listener(suc, err)
            ),
            "link_credential_listener"
        )
        task.addOnCompleteListener(self.link_credential_listener)

    def delete_user(self, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.delete()
        self.user_delete_listener = self.__construct_user_callback(
            listener, "user_delete_listener")
        task.addOnCompleteListener(self.user_delete_listener)

    def reauthenticate(self, credential, listener=lambda *_: None):
        user = self.get_current_user()
        task = user.reauthenticate(credential)
        self.user_reauthenticate_listener = self.__construct_user_callback(
            listener, "user_reauthenticate_listener")
        task.addOnCompleteListener(self.user_reauthenticate_listener)


class FirestoreMixin(__BaseMixin):
    firestore_listeners = []
    last_visible = {}

    def __construct_set_callback(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    None if task.isSuccessful()
                    else task.getException().getMeesage()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_get_document_callback(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    {
                        **serialize(task.getResult().getData()),
                        "document_id": task.getResult().getId()
                    }
                    if task.isSuccessful()
                    else task.getException().getMessage()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_get_collection_callback(self, listener):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    [
                        {
                            **serialize(document.getData()),
                            "document_id": document.getId()
                        }
                        for document in task.getResult()
                    ] if task.isSuccessful()
                    else task.getException().getMessage()
                ),
                self.firestore_listeners.remove(callback)
            )
        )
        self.firestore_listeners.append(callback)
        return callback

    def __construct_document_snapshot_callback(self, listener):
        callback = self.event_listener(
            lambda snapshot, error:
            listener(
                error.toString() if not is_jnull(error)
                else {**serialize(snapshot.getData()), "document_id": snapshot.getId()}
                if not is_jnull(snapshot) and snapshot.exists()
                else None,
                "Local" if not is_jnull(snapshot) and snapshot.getMetadata().hasPendingWrites()
                else "Server"
            )
        )
        return callback

    def __construct_collection_snapshot_callback(self, listener, listen_for_changes):
        Type = autoclass("com.google.firebase.firestore.DocumentChange$Type")
        callback = self.event_listener(
            lambda snapshot, error:
            listener(
                error.toString() if not is_jnull(error)
                else [
                    {
                        **serialize(document.getDocument().getData()),
                        "document_id": document.getDocument().getId(),
                        "document_type":
                            "ADDED" if document.getType().ordinal() == Type.ADDED.ordinal() else
                            "MODIFIED" if document.getType().ordinal() == Type.MODIFIED.ordinal() else
                            "REMOVED"
                    }
                    for document in snapshot.getDocumentChanges()
                ] if listen_for_changes else [
                    {**serialize(document.getData()), "document_id": document.getId()}
                    for document in snapshot
                ],
                "Local" if not is_jnull(snapshot) and snapshot.getMetadata().hasPendingWrites()
                else "Server"
            )
        )
        return callback

    def __construct_pagination_of_document_callback(self, listener, collection_path):
        callback = self.on_complete_listener(
            lambda task:
            (
                listener(
                    task.isSuccessful(),
                    [
                        {
                            **serialize(document.getData()),
                            "document_id": document.getId()
                        }
                        for document in task.getResult()
                    ] if task.isSuccessful()
                    else task.getException().toString()
                ),
                self.firestore_listeners.remove(callback),
                self.last_visible.update(
                    {
                        collection_path:
                            task.getResult().getDocuments().get(
                                size - 1
                            )
                    }
                ) if (size := task.getResult().size()) == 0 else None,
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
                return
            case _:
                raise Exception("source must be 'default' or 'server' or 'cache'")
        return source

    def collection(self, path):
        db = self.firestore.get_db()
        return db.collection(path)

    def document(self, path):
        db = self.firestore.get_db()
        return db.document(path)

    def add_document(self, collection_path, data, listener=lambda *_: None):
        (
            self.collection(collection_path)
            .add(serialize(data))
            .addOnCompleteListener(self.__construct_set_callback(listener))
        )

    def set_document(self, document_path, data, listener, merge=False):
        document = self.document(document_path)
        if merge:
            SetOptions = autoclass("com.google.firebase.firestore.SetOptions")
            document = document.set(serialize(data), SetOptions.merge())
        else:
            document = document.set(serialize(data))
        document.addOnCompleteListener(self.__construct_set_callback(listener))

    def update_document(
            self,
            document_path: str,
            data: list | dict,
            listener: Callable[[bool, None | str], None]
    ) -> None:
        if isinstance(data, dict):
            data = chain.from_iterable(data.items())
        (
            self.document(document_path)
            .update(*serialize(data, raw_python=True))
            .addOnCompleteListener(self.__construct_set_callback(listener))
        )

    def delete_document(self, document_path, listener=lambda *_: None):
        (
            self.document(document_path)
            .delete()
            .addOnCompleteListener(self.__construct_set_callback(listener))
        )

    def get_document(self, document_path, listener, source=None):
        source = self.__set_source__(source)
        document = self.document(document_path)
        if source:
            document = document.get(source)
        else:
            document = document.get()
        document.addOnCompleteListener(self.__construct_get_document_callback(listener))

    def get_collection_of_documents(self, collection_path, listener, source=None):
        source = self.__set_source__(source)
        collection = self.collection(collection_path)
        if source:
            collection = collection.get(source)
        else:
            collection = collection.get()
        collection.addOnCompleteListener(self.__construct_get_collection_callback(listener))

    def add_document_snapshot_listener(self, document_path, listener):
        callback = self.__construct_document_snapshot_callback(listener)
        listener_registration = (
            self.document(document_path)
            .addSnapshotListener(callback)
        )
        self.listener_registration[document_path] = [callback, listener_registration]

    def add_collection_snapshot_listener(self, collection_path, listener, listen_for_changes=True):
        callback = self.__construct_collection_snapshot_callback(listener, listen_for_changes)
        listener_registration = (
            self.collection(collection_path)
            .addSnapshotListener(callback)
        )
        self.listener_registration[collection_path] = [callback, listener_registration]

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
            self.__construct_pagination_of_document_callback(listener, collection_path))

    def where(self, collection_path, filter_, listener, listen_for_changes=True, source=None, snapshot=False):
        source = self.__set_source__(source)
        collection = self.collection(collection_path)
        query = collection.where(filter_)
        if not snapshot:
            if source:
                query = query.get(source)
            else:
                query = query.get()
            query.addOnCompleteListener(self.__construct_get_collection_callback(listener))
        else:
            callback = self.__construct_collection_snapshot_callback(listener, listen_for_changes)
            listener_registration = query.addSnapshotListener(callback)
            self.listener_registration[collection_path] = [callback, listener_registration]


class DatabaseMixin(__BaseMixin):
    database_listeners = []
    last_visible = {}

    def __construct_completion_callback(self, listener):
        callback = self.completion_listener(
            lambda error, ref:
            (
                listener(
                    error.getMessage() if error else None,
                    ref
                ),
                self.database_listeners.remove(callback)
            )
        )
        self.database_listeners.append(callback)
        return callback

    def __construct_on_complete_listener(self, listener):
        callback = self.on_complete_listener(
            lambda task: (
                listener(
                    task.isSuccessful(),
                    self.__process_task(task)
                ),
                self.database_listeners.remove(callback)
            )
        )
        self.database_listeners.append(callback)
        return callback

    @staticmethod
    def __process_task(task):
        if task.isSuccessful() and (result := task.getResult()):
            if children := result.getChildren():
                return [
                    {"key": data.getKey(), **serialize(data.getValue())}
                    for data in children
                ]
            return {**serialize(result.getValue()), "key": result.getKey()}

    def __construct_transaction_handler(self, transaction, on_complete):
        callback = self.transaction_handler(
            lambda mutable_data: self.__do_transaction(transaction, mutable_data),
            lambda error, committed, current_data: (
                on_complete(
                    None if is_jnull(error) else error.getDetails(),
                    committed,
                    current_data
                ),
                self.database_listeners.remove(callback),
                delattr(self, "_transaction_result")
            )
        )
        self.database_listeners.append(callback)
        return callback

    def __construct_value_event_listener(self, on_data_changed, on_canceled, r_type):
        callback = self.value_event_listener(
            on_data_changed=lambda data_snapshot: (
                on_data_changed(self.__process_data_snapshot(data_snapshot, r_type)),
            ),
            on_cancelled=lambda error: on_canceled(error.getMessage())
        )
        return callback

    def __do_transaction(self, transaction, mutable_data):
        if (data := mutable_data.getValue()) is None:
            return Transaction.success(mutable_data)
        new_data = transaction(serialize(data))
        if not new_data:
            self._transaction_result = Transaction.abort()
        else:
            mutable_data.setValue(serialize(new_data))
            self._transaction_result = Transaction.success(mutable_data)
        return self._transaction_result

    @staticmethod
    def __process_data_snapshot(snapshot, r_type):
        if (data := snapshot.getValue()) is None:
            return
        if r_type == "dict":
            if not isinstance(serialized_data := serialize(data), dict):
                return {snapshot.getKey(): serialized_data}
            return {"key": snapshot.getKey(), **serialized_data}
        else:
            new_data = []
            for data in snapshot.getChildren():
                if not isinstance(serialized_data := serialize(data.getValue()), dict):
                    serialized_data = {data.getKey(), serialized_data}
                else:
                    serialized_data["key"] = data.getKey()
                new_data.append(serialized_data)
            return new_data

    def get_instance(self):
        db = self.database
        return db.get_db()

    def get_reference(self, path=None):
        db = self.get_instance()
        if path:
            return db.getReference(path)
        return db.getReference()

    def set_persistence_enabled(self, enabled: bool):
        self.get_instance().setPersistenceEnabled(enabled)

    def add_value_event_listener(self, path_or_query, on_data_changed, on_canceled=lambda error: None, r_type="list"):
        callback = self.__construct_value_event_listener(on_data_changed, on_canceled, r_type)
        Query = autoclass("com.google.firebase.database.Query")
        if not Query._class.isInstance(path_or_query):
            db = self.get_reference(path_or_query)
            db.addValueEventListener(callback)
        else:
            db = path_or_query
            db.addValueEventListener(callback)
        self.value_event_listeners[path_or_query] = [callback, db]

    def add_listener_for_single_value_event(self, path_or_query, on_data_changed, on_canceled=lambda error: None):
        callback = self.__construct_value_event_listener(on_data_changed, on_canceled)
        Query = autoclass("com.google.firebase.database.Query")
        if not Query._class.isInstance(path_or_query):
            db = self.get_reference(path_or_query)
            db.addListenerForSingleValueEvent(callback)
        else:
            db = path_or_query
            db.addListenerForSingleValueEvent(callback)
        self.value_event_listeners[path_or_query] = [callback, db]

    def get(self, query, listener):
        callback = self.__construct_on_complete_listener(listener)
        task = query.get()
        task.addOnCompleteListener(callback)

    def get_key(self, path):
        return self.get_reference(path).getKey()

    def get_parent(self, path):
        return self.get_reference(path).getParent()

    def get_root(self, path):
        return self.get_reference(path).getRoot()

    def go_offline(self, path):
        self.get_reference(path).goOffline()

    def go_online(self, path):
        self.get_reference(path).goOnline()

    def on_disconnect(self, path):
        return self.get_reference(path).onDisconnect()

    def push(self, path):
        return self.get_reference(path).push()

    def remove_value(self, path, listener=lambda *_: None):
        callback = self.__construct_on_complete_listener(listener)
        task = self.get_reference(path).removeValue()
        task.addOnCompleteListener(callback)

    def run_transaction(self, path, do_transaction, on_complete=lambda *_: None):
        handler = self.__construct_transaction_handler(do_transaction, on_complete)
        self.get_reference(path).runTransaction(handler)

    def set_value(self, path, data, listener=lambda *_: None):
        if isinstance(data, (dict, list)):
            data = serialize(data)
        callback = self.__construct_on_complete_listener(listener)
        task = self.get_reference(path).setValue(data)
        task.addOnCompleteListener(callback)

    def update_children(self, path, data, listener=lambda *_: None):
        callback = self.__construct_on_complete_listener(listener)
        task = self.get_reference(path).updateChildren(serialize(data))
        task.addOnCompleteListener(callback)

    def update_children_simultaneously(self, data, listener=lambda *_: None):
        callback = self.__construct_on_complete_listener(listener)
        task = self.get_reference().updateChildren(serialize(data))
        task.addOnCompleteListener(callback)


class StorageMixin(__BaseMixin):
    storage_listeners = []

    def __construct_on_complete_listener(self, listener):
        callback = self.on_complete_listener(
            lambda task: (
                listener(
                    task.isSuccessful(),
                    self.__process_task(task)
                ),
                self.storage_listeners.remove(callback),
                delattr(self, "_url_task")
            )
        )
        self.storage_listeners.append(callback)
        return callback

    def __construct_continuation(self):
        callback = self.continuation(lambda task: self.__process_url_task(task, callback))
        self.storage_listeners.append(callback)
        return callback

    @staticmethod
    def __process_task(task):
        if task.isSuccessful():
            return task.getResult().toString()
        return task.getException().getMessage()

    def __process_url_task(self, task, callback):
        self.storage_listeners.remove(callback)
        if not task.isSuccessful():
            raise JavaException(task.getException().getMessage())
        self._url_task = task.getResult().getStorage().getDownloadUrl()
        return self._url_task

    def get_download_url(self, path, listener=lambda *_: None):
        ref = self.get_reference(path)
        task = ref.getDownloadUrl()
        task.addOnCompleteListener(self.__construct_on_complete_listener(listener))

    def get_download_url_from_task(self, task, listener):
        print(task.isSuccessful())
        if task.isSuccessful():
            task.getResult() \
                .getStorage() \
                .getDownloadUrl() \
                .addOnCompleteListener(self.__construct_on_complete_listener(listener))

    def get_instance(self):
        return self.storage.get_instance()

    def get_reference(self, path=None):
        storage = self.get_instance()
        if path:
            return storage.getReference(path)
        return storage.getReference()

    def put_bytes(self, path, data, listener=lambda *_: None):
        ref = self.get_reference(path)
        task = ref.putBytes(data)
        task.continueWithTask(self.__construct_continuation()) \
            .addOnCompleteListener(self.__construct_on_complete_listener(listener))

    def put_stream(self, path, stream, listener=lambda *_: None):
        ref = self.get_reference(path)
        task = ref.putStream(stream)
        task.continueWithTask(self.__construct_continuation()) \
            .addOnCompleteListener(self.__construct_on_complete_listener(listener))

    def put_file(self, path, file, listener=lambda *_: None):
        ref = self.get_reference(path)
        task = ref.putFile(file)
        task.continueWithTask(self.__construct_continuation()) \
            .addOnCompleteListener(self.__construct_on_complete_listener(listener))


class PhoneMixin(__BaseMixin):
    _callback = None
    _state_change = None

    def set_phone_state_callbacks(self, on_code_sent, on_verification_completed, on_verification_failed):
        self._callback = VerificationStateChangeCallback(
            on_code_sent,
            on_verification_completed,
            lambda e: on_verification_failed(e.getMessage()),
        )
        self._state_change = autoclass("com.simplejnius.sjfirebase.callback.VerificationStateChange")()
        self._state_change.setCallback(self._callback)
        return self._state_change

    @staticmethod
    def _long(num):
        return autoclass("java.lang.Long")(num)

    def start_phone_number_verification(self, phone_number, timeout, listener):
        self.phone.startPhoneNumberVerification(
            phone_number,
            self._long(timeout),
            _activity,
            listener,
        )

    def resend_verification_code(self, phone_number, timeout, token, listener):
        self.phone.resendVerificationCode(
            phone_number,
            self._long(timeout),
            _activity,
            listener,
            token
        )

    def verify_number_with_code(self, verification_id, code):
        return self.phone.verifyPhoneNumberWithCode(verification_id, code)


class FunctionMixin(__BaseMixin):
    function_listeners = []

    def __construct_on_complete_listener(self, listener):
        callback = self.on_complete_listener(
            lambda task: (
                listener(
                    task.isSuccessful(),
                    self.__process_task(task)
                ),
                self.function_listeners.remove(callback)
            )
        )
        self.function_listeners.append(callback)
        return callback

    def __process_task(self, task):
        if task.isSuccessful():
            return serialize(task.getResult().getData())
        FirebaseFunctionsException = autoclass("com.google.firebase.functions.FirebaseFunctionsException")
        exc = task.getException()
        if FirebaseFunctionsException._class.isInstance(exc):
            e = cast("com.google.firebase.functions.FirebaseFunctionsException", exc)
            return e.getCode(), e.getDetails(), exc.getMessage()

    def get_https_callable_call(self, function_name, data=None, listener=lambda *_: None):
        callback = self.__construct_on_complete_listener(listener)
        instance = self.functions.getInstance()
        ref = instance.getHttpsCallable(function_name)
        if data:
            task = ref.call(serialize(data))
        else:
            task = ref.call()
        task.addOnCompleteListener(callback)
