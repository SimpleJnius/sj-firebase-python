# sj-firebase-python
 Implement Firebase Java SDK in Python

*[Firebase](https://firebase.google.com/)*
> Make your app the
> best it can be
> 
> Firebase is an app development platform that helps you build and grow apps and games users love. 
> Backed by Google and trusted by millions of businesses around the world.

## Usage
### Buildozer Android project
```properties
android.gradle_dependencies = io.github.simplejnius:sjfirebase:0.3.0
requirements = https://github.com/SimpleJnius/sj-firebase-python/archive/refs/heads/master.zip
```
The current version of [python-for-android](https://github.com/kivy/python-for-android) 
lacks support for incorporating bom dependencies, modifying the classpath, and copying the `google-service.json`. 
To address this limitation, a fork of python-for-android has been developed to include these functionalities. 
To implement these changes in your `buildozer.spec` file, 
make adjustments to the specified section using the provided values below:
```properties
android.api = 34
android.enable_androidx = True
android.gradle_dependencies = io.github.simplejnius:sjfirebase:1.0.0,
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