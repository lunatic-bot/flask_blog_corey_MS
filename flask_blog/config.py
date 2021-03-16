class Config():
	SECRET_KEY = '97cf8017306c30dc1d8c15ce776c6b87' #should import from environment variable
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #should import from environment variable
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'arpitbjp771@gmail.com' #should import from environment variable
	MAIL_PASSWORD = 'programminginc' #should import from environment variable