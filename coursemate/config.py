class DevConfig:
    DEVELOPTMENT = True

    # AWS S3
    S3_KEY = ''
    S3_SECRET = ''
    S3_BUCKET = 'coursemat' # typo?
    S3_UPLOAD_DIRECTORY = 'Testing'
    SECRET_KEY = 'TestingSecretKey'

    # SQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/CourseMate'
