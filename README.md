# sj-firebase-python
 Implement Firebase Java SDK in Python

 <!-- GitAds-Verify: V1Y658YQ4CT1W7YNRP6RCUDTVARQMDOM -->
 ## GitAds Sponsored
[![Sponsored by GitAds](https://gitads.dev/v1/ad-serve?source=simplejnius/sj-firebase-python@github)](https://gitads.dev/v1/ad-track?source=simplejnius/sj-firebase-python@github)



*[Firebase](https://firebase.google.com/)*
> Make your app the
> best it can be
> 
> Firebase is an app development platform that helps you build and grow apps and games users love. 
> Backed by Google and trusted by millions of businesses around the world.

## Usage
### Buildozer Android project
```properties
android.gradle_dependencies = io.github.simplejnius:sjfirebase:1.3.2
requirements = sjfirebase
```
The current version of [python-for-android](https://github.com/kivy/python-for-android) 
lacks support for incorporating bom dependencies, modifying the classpath, and copying the `google-service.json`. 
To address this limitation, a fork of python-for-android has been developed to include these functionalities. 
To implement these changes in your `buildozer.spec` file, 
make adjustments to the specified section using the provided values below:
```properties
android.api = 34
android.enable_androidx = True
android.gradle_dependencies = io.github.simplejnius:sjfirebase:1.3.2,
    com.google.firebase:firebase-auth,com.google.firebase:firebase-database,
    com.google.firebase:firebase-firestore,com.google.firebase:firebase-storage,
    com.google.firebase:firebase-analytics
p4a.fork = SimpleJnius
p4a.branch = firebase
```
**Important Note:** Upon creating an Android project within your [Firebase Console](https://firebase.google.com), 
ensure to transfer the `google-service.json` file to the same location as your `main.py` file.
#### Python(Buildozer) installation
```shell
# pip
pip install sjfirebase

# buildozer.spec
requirements = sjfirebase
```

## Sample Code Documentation

**To add, set, update, and delete a document in a collection**
```python
from kivy.uix.screenmanager import Screen  # noqa
from sjfirebase.tools.mixin import FirestoreMixin


class MyScreen(Screen, FirestoreMixin):
    
    def on_event1(self):
        data = dict(name=self.ids.name.text, email=self.ids.email.text)
        
        # creates a new document in "individual" collection and
        # passes a success(True/False) and error(None or FirebaseException)
        # parameters to your callback
        self.add_document("individuals", data, lambda success, error: print(success, error))
    
    def on_event2(self):
        data = dict(name=self.ids.name.text, email=self.ids.email.text)
        
        # creates a new or overwrite document "custom_document_id" in collection
        # and passes a success(True/False) and error(None or FirebaseException)
        # parameters to your callback
        self.set_document("individual/custom_document_id", data, lambda success, error: print(success, error))
    
    def on_event3(self):
        data = dict(name=self.ids.name.text, email=self.ids.email.text)
        
        # creates a new or update document "custom_document_id" in collection
        # and passes a success(True/False) and error(None or FirebaseException)
        # parameters to your callback
        self.set_document("individual/custom_document_id", data, lambda success, error: print(success, error), merge=True)
    
    def on_event4(self):
        data = ["name", self.ids.name.text, "email", self.ids.email.text]
        
        # creates a new or overwrite document "custom_document_id" in collection
        # and passes a success(True/False) and error(None or FirebaseException)
        # parameters to your callback.
        # Notice the data is a list, and this list must be an even length and not odd length.
        # Every odd values are the key while the even values are the value.
        # E.g in the above `data` `name` is the key while `self.ids.name.text` is the value
        # same goes with the email. It's this way due to the varargs nature of the Firestore `update` method
        # signature
        self.update_document("individual/custom_document_id", data, lambda success, error: print(success, error))
        
    def on_event5(self):
        # deletes document "custom_document_id"
        self.delete_document("individual/custom_document_id", lambda success, error: print(success, error))

# NB: You can instantiate the FirestoreMixing directly
# E.g
f = FirestoreMixin()
f.add_document(...)
f.set_document(...)
# etc..
```

**To get-data, paginate-data, and get-realtime-updates**
```python
from kivy.uix.screenmanager import Screen  # noqa
from sjfirebase.tools.mixin import FirestoreMixin


class MyScreen(Screen, FirestoreMixin):
    def on_event1(self):
        # gets a dictionary of data from "document_id" if any data and passes
        # `success` (True/False) and `data` (dict/errorMessage).
        # always check if success is True before accessing items from data,
        # or check if data is an instance of dict. Else log the data to see the error message
        self.get_document("individual/document_id", lambda success, data: print(success, data))
    
    def on_event2(self):
        # everything @on_event1 plus `source` that states where the data should be fetched.
        # either cache, server or default. cache gets from firebase data stored locally
        # on the device for offline purposes while server gets from firebase cloud directly.
        # default can be either cache or cloud depending on your configuration.
        self.get_document("individual/document_id", lambda success, data: print(success, data), source="cache")
    
    def on_event3(self):
        # gets all document at "individual" collection and passes success and data argument.
        # here, data is a list of dict. before accessing, refer to @on_event1
        self.get_collection_of_documents("individual", lambda success, data: print(success, data))
    
    def on_event4(self):
        # refer to @on_event2 for "source" and @on_event3 for functionality description
        self.get_collection_of_documents("individual", lambda success, data: print(success, data), source="cache")

    def on_event5(self):
        # refer to @on_event3 for functionality description. The new thing here is `limit`.
        # limit is used to limit the amount of data you fetch from firebase and paginate as you go.
        self.get_pagination_of_documents("individual", 10, lambda success, data: print(success, data))

    def on_event6(self):
        # listens for document changes and returns a dict of data and location
        # where the data is coming from. `data`(dict/errorMessage), where("Local"/"Server")
        self.add_document_snapshot_listener("individual/document_id", lambda data, where: print(data, where))
    
    def on_event7(self):
        # same as @on_event6 but gets a list of document with information on whether they were
        # added, removed or modified
        self.add_collection_snapshot_listener("individual", lambda data, where: print(data, where))
```


### Python API
#### ActionCodeSettings
```python
class sjfirebase.jclass.action.ActionCodeSettings
```
Structure that contains the required continue/state URL with optional Android and iOS bundle identifiers. 
The stateUrl used to initialize this class is the link/deep link/fallback url used while constructing the 
Firebase dynamic link.

**methods**
- `newBuilder`
##### Visit [ActionCodeSettings Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/ActionCodeSettings) for more API

#### SJFirebaseAuthEmai
```python
class sjfirebase.jclass.emailauth.SJFirebaseAuthEmail
```
The entry point of the Firebase Authentication SDK.
First, obtain an instance of this class by calling `get_instance`

**methods**
- check_user_signed_in
- get_instance
##### Visit [FirebaseAuth Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth) for more API

#### SJFirebaseDatabase
```python
class sjfirebase.jclass.database.SJFirebaseDatabase
```
The entry point for accessing a Firebase Database. 
You can get an instance by calling getInstance. 
To access a location in the database and read or write data, use `get_ref`

**methods**
- get_db
- get_ref
##### Visit [FirebaseDatabase Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/database/FirebaseDatabase) for more API

#### SJFirebaseFirestore
```python
class sjfirebase.jclass.firestore.SJFirebaseFirestore
```

**methods**
- get_db
##### Visit [FirebaseFirestore Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore) for more API

#### SJFirebaseUser
```python
class sjfirebase.jclass.user.SJFirebaseUser
```
Represents a user's profile information in your Firebase project's user database. 
It also contains helper methods to change or retrieve profile information, 
as well as to manage that user's authentication state.

**methods**
- get_current_user
- profile_change_request_builder
##### Visit [FirebaseUser Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser) for more API

#### SJFirebaseStorage
```python
class sjfirebase.jclass.user.SJFirebaseStorage
```
FirebaseStorage is a service that supports uploading and downloading large objects
to Google Cloud Storage. Pass a custom instance of FirebaseApp to get_instance which
will initialize it with a storage location (bucket) specified via setStorageBucket.

Otherwise, if you call getReference without a FirebaseApp, the FirebaseStorage instance
will initialize with the default FirebaseApp obtainable from get_instance. The storage
location in this case will come the JSON configuration file downloaded from the web

**methods**
- get_instance
##### Visit [FirebaseStorage Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/storage/FirebaseStorage) for more API

#### OnCompleteListener
```python
class sjfirebase.jinterface.google

OnCompleteListener
```
Listener called when a Task completes.

**methods**
- onComplete
##### Visit [OnCompleteListener Documentation](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener) for more API

#### ValueEventListener
```python
class sjfirebase.jinterface.firebase.ValueEventListener
```

**methods**
- onDataChange
- onCancelled
##### Visit [ValueEventListener Documentation](https://firebase.google.com/docs/reference/android/com/google/firebase/database/ValueEventListener) for more API
