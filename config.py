# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://goat:sam4core@goathub.cjobi9tevpql.us-west-2.rds.amazonaws.com:3306/goathub'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = '6qNFknUx3zp8BXSCf16P++rzGMu+L8SmjPMJE1c3'