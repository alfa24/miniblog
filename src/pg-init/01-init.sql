CREATE USER pgadmin WITH LOGIN PASSWORD 'admin123456*';
CREATE DATABASE docker;
GRANT ALL PRIVILEGES ON DATABASE docker TO pgadmin;
