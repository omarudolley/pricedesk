from app.constants import GOOGLE_DRIVE_PATH_PREFIX, GOOGLE_DRIVE_PATH_SUFFIX


def generate_google_drive_url(doc_id: str):
    return GOOGLE_DRIVE_PATH_PREFIX + doc_id + GOOGLE_DRIVE_PATH_SUFFIX
