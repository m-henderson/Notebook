# Date: 02/07/2019
# Author: Mohamed
# Description: Const

from enum import Enum


class PermissionConst(Enum):

    ROOT = 0 # can view, delete, logout, change permissions of users
    VIEW = 1 # can view, users
    NONE = 2 # normal user


class DatabaseConst(Enum):

    PROFILE_DB = 'lib/database/profile.db'
    ACCOUNT_DB = 'lib/database/account.db'

    LOCK_TIME = 60 * 60 # (secs) 60 * 60 => 1 hour
    MAX_FAILED_ATTEMPTS = 7 # attempts before locking


class SessionConst(Enum):

    SESSION_TTL = 2 # (mins) 2 => 2 minutes


class CredentialConst(Enum):

    MIN_USERNAME_LENGTH = 4
    MAX_USERNAME_LENGTH = 32

    MIN_PASSWORD_LENGTH = 12
    MAX_PASSWORD_LENGTH = 64 


class ProfileConst(Enum):

    MIN_NOTE_LENGTH = 4
    MAX_NOTE_LENGTH = 32

    MIN_TOPIC_LENGTH = 4
    MAX_TOPIC_LENGTH = 32