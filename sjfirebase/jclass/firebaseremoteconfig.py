# Auto-generated full reflection for com.google.firebase.remoteconfig.FirebaseRemoteConfig
# Source: javap -s output

from jnius import (
    JavaClass,
    MetaJavaClass,
    JavaMethod,
    JavaStaticMethod,
    JavaStaticField,
    JavaMultipleMethod,
)


class FirebaseRemoteConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/firebase/remoteconfig/FirebaseRemoteConfig"

    # constructors (signature, is_varargs)
    __javaconstructor__ = [
        (
            "(Landroid/content/Context;"
            "Lcom/google/firebase/FirebaseApp;"
            "Lcom/google/firebase/installations/FirebaseInstallationsApi;"
            "Lcom/google/firebase/abt/FirebaseABTesting;"
            "Ljava/util/concurrent/Executor;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigCacheClient;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigCacheClient;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigCacheClient;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigFetchHandler;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigGetParameterHandler;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigSharedPrefsClient;"
            "Lcom/google/firebase/remoteconfig/internal/ConfigRealtimeHandler;"
            "Lcom/google/firebase/remoteconfig/internal/rollouts/RolloutsStateSubscriptionsHandler;)V",
            False,
        ),
    ]

    # static fields
    DEFAULT_VALUE_FOR_BOOLEAN = JavaStaticField("Z")
    DEFAULT_VALUE_FOR_BYTE_ARRAY = JavaStaticField("[B")
    DEFAULT_VALUE_FOR_DOUBLE = JavaStaticField("D")
    DEFAULT_VALUE_FOR_LONG = JavaStaticField("J")
    DEFAULT_VALUE_FOR_STRING = JavaStaticField("Ljava/lang/String;")
    LAST_FETCH_STATUS_FAILURE = JavaStaticField("I")
    LAST_FETCH_STATUS_NO_FETCH_YET = JavaStaticField("I")
    LAST_FETCH_STATUS_SUCCESS = JavaStaticField("I")
    LAST_FETCH_STATUS_THROTTLED = JavaStaticField("I")
    TAG = JavaStaticField("Ljava/lang/String;")
    VALUE_SOURCE_DEFAULT = JavaStaticField("I")
    VALUE_SOURCE_REMOTE = JavaStaticField("I")
    VALUE_SOURCE_STATIC = JavaStaticField("I")

    # methods (grouped by name; overloads use JavaMultipleMethod)
    activate = JavaMethod("()Lcom/google/android/gms/tasks/Task;")
    addOnConfigUpdateListener = JavaMethod(
        "(Lcom/google/firebase/remoteconfig/ConfigUpdateListener;)"
        "Lcom/google/firebase/remoteconfig/ConfigUpdateListenerRegistration;"
    )
    ensureInitialized = JavaMethod("()Lcom/google/android/gms/tasks/Task;")
    fetch = JavaMultipleMethod(
        [
            ("()Lcom/google/android/gms/tasks/Task;", False, False),
            ("(J)Lcom/google/android/gms/tasks/Task;", False, False),
        ]
    )
    fetchAndActivate = JavaMethod("()Lcom/google/android/gms/tasks/Task;")
    getAll = JavaMethod("()Ljava/util/Map;")
    getBoolean = JavaMethod("(Ljava/lang/String;)Z")
    getDouble = JavaMethod("(Ljava/lang/String;)D")
    getInfo = JavaMethod(
        "()Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigInfo;"
    )
    getInstance = JavaMultipleMethod(
        [
            ("()Lcom/google/firebase/remoteconfig/FirebaseRemoteConfig;", True, False),
            (
                "(Lcom/google/firebase/FirebaseApp;)Lcom/google/firebase/remoteconfig/FirebaseRemoteConfig;",
                True,
                False,
            ),
        ]
    )
    getKeysByPrefix = JavaMethod("(Ljava/lang/String;)Ljava/util/Set;")
    getLong = JavaMethod("(Ljava/lang/String;)J")
    getRolloutsStateSubscriptionsHandler = JavaMethod(
        "()Lcom/google/firebase/remoteconfig/internal/rollouts/RolloutsStateSubscriptionsHandler;"
    )
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getValue = JavaMethod(
        "(Ljava/lang/String;)Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigValue;"
    )
    reset = JavaMethod("()Lcom/google/android/gms/tasks/Task;")
    schedule = JavaMethod("(Ljava/lang/Runnable;)V")
    setConfigSettingsAsync = JavaMethod(
        "(Lcom/google/firebase/remoteconfig/FirebaseRemoteConfigSettings;)Lcom/google/android/gms/tasks/Task;"
    )
    setConfigUpdateBackgroundState = JavaMethod("(Z)V")
    setCustomSignals = JavaMethod(
        "(Lcom/google/firebase/remoteconfig/CustomSignals;)Lcom/google/android/gms/tasks/Task;"
    )
    setDefaultsAsync = JavaMultipleMethod(
        [
            ("(Ljava/util/Map;)Lcom/google/android/gms/tasks/Task;", False, False),
            ("(I)Lcom/google/android/gms/tasks/Task;", False, False),
        ]
    )
    startLoadingConfigsFromDisk = JavaMethod("()V")
    toExperimentInfoMaps = JavaStaticMethod("(Lorg/json/JSONArray;)Ljava/util/List;")
    updateAbtWithActivatedExperiments = JavaMethod("(Lorg/json/JSONArray;)V")
