"""
Python binding for the Firebase Auth GoogleAuthProvider and GoogleAuthCredential classes.

This module provides PyJNIus bindings for the com.google.firebase.auth.GoogleAuthProvider
and com.google.firebase.auth.GoogleAuthCredential Java classes. It allows Python code to
interact with Google authentication in Firebase.

The GoogleAuthProvider class provides static methods for creating Google authentication
credentials, while the GoogleAuthCredential class represents a credential from Google
that can be used for Firebase authentication.
"""

from jnius import JavaClass, MetaJavaClass, JavaStaticMethod, JavaMethod, JavaStaticField

__all__ = ("GoogleAuthProvider", "GoogleAuthCredential")


class GoogleAuthProvider(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.auth.GoogleAuthProvider Java class.
    
    This class provides a PyJNIus interface to the Firebase GoogleAuthProvider class,
    which offers static methods for creating Google authentication credentials.
    """
    __javaclass__ = "com/google/firebase/auth/GoogleAuthProvider"
    
    PROVIDER_ID = JavaStaticField("Ljava/lang/String;")
    """
    Static field representing the provider ID for Google authentication.
    
    This constant is used to identify Google as the authentication provider.
    """
    
    GOOGLE_SIGN_IN_METHOD = JavaStaticField("Ljava/lang/String;")
    """
    Static field representing the sign-in method for Google authentication.
    
    This constant is used to identify the Google sign-in method.
    """
    
    getCredential = JavaStaticMethod(
        "(Ljava/lang/String;Ljava/lang/String;)"
        "Lcom/google/firebase/auth/AuthCredential;"
    )
    """
    Creates a Google authentication credential from an ID token and access token.
    
    Parameters:
        idToken: The Google ID token.
        accessToken: The Google access token.
        
    Returns:
        An AuthCredential object that can be used for Firebase authentication.
    """


class GoogleAuthCredential(JavaClass, metaclass=MetaJavaClass):
    """
    Python binding for the com.google.firebase.auth.GoogleAuthCredential Java class.
    
    This class provides a PyJNIus interface to the Firebase GoogleAuthCredential class,
    which extends AuthCredential and represents a credential from Google that can be
    used for Firebase authentication.
    """
    __javaclass__ = "com/google/firebase/auth/GoogleAuthCredential"
    
    __javaconstructor__ = [
        ('(Ljava/lang/String;Ljava/lang/String;)V', False)
    ]
    """
    Java constructor for the GoogleAuthCredential class.
    
    Parameters:
        idToken: The Google ID token.
        accessToken: The Google access token.
    """
    
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    """
    Static field for the Parcelable.Creator used to create instances of GoogleAuthCredential
    from a Parcel.
    """
    
    getProvider = JavaMethod("()Ljava/lang/String;")
    """
    Returns the provider ID for this credential.
    
    Returns:
        A string representing the provider ID (e.g., "google.com").
    """
    
    getSignInMethod = JavaMethod("()Ljava/lang/String;")
    """
    Returns the sign-in method for this credential.
    
    Returns:
        A string representing the sign-in method.
    """
    
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    """
    Writes this GoogleAuthCredential to a Parcel.
    
    This method is used for Android's Parcelable implementation to serialize the object.
    
    Parameters:
        parcel: The Parcel to write to.
        flags: Additional flags about how the object should be written.
    """
