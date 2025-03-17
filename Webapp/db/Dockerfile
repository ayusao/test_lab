# # Use official MySQL image
# FROM mysql:8.0

# # Set environment variables 
# ENV MYSQL_ROOT_PASSWORD=rootpassword
# ENV MYSQL_DATABASE=testdb
# ENV MYSQL_USER=testuser
# ENV MYSQL_PASSWORD=TestPassword12!

# # Copy the SQL script only if it exists
# COPY init.sql /docker-entrypoint-initdb.d/
# # Expose MySQL port
# EXPOSE 3306

# # Default MySQL command
# CMD ["mysqld"]


FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=testdb

COPY init.sql /docker-entrypoint-initdb.d/