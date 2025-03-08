# chevereto图床docker-compose

```yml
services:
  chevereto:
    image: chevereto/chevereto
    container_name: chevereto
    restart: unless-stopped
    ports:
      - "8082:80"
    environment:
      CHEVERETO_DB_HOST: db
      CHEVERETO_DB_USER: chevereto
      CHEVERETO_DB_PASS: chevereto_password
      CHEVERETO_DB_NAME: chevereto
    depends_on:
      - db
    volumes:
      - chevereto_images:/var/www/html/images
      - chevereto_config:/var/www/html

  db:
    image: mariadb:10.5
    container_name: chevereto_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: chevereto
      MYSQL_USER: chevereto
      MYSQL_PASSWORD: chevereto_password
    volumes:
      - chevereto_db:/var/lib/mysql

volumes:
  chevereto_images:
  chevereto_config:
  chevereto_db:
```  

## 如何迁移数据

你的数据存储在 Docker 卷里，迁移时只需备份这些卷：  
```shell
docker-compose down
docker volume create chevereto_images
docker volume create chevereto_config
docker volume create chevereto_db
```  
然后复制旧数据：  
```shell
docker run --rm -v chevereto_images:/data -v $(pwd):/backup alpine tar czf /backup/chevereto_images.tar.gz -C /data .
docker run --rm -v chevereto_config:/data -v $(pwd):/backup alpine tar czf /backup/chevereto_config.tar.gz -C /data .
docker run --rm -v chevereto_db:/data -v $(pwd):/backup alpine tar czf /backup/chevereto_db.tar.gz -C /data .
```  
恢复数据：  
```shell
docker run --rm -v chevereto_images:/data -v $(pwd):/backup alpine tar xzf /backup/chevereto_images.tar.gz -C /data
docker run --rm -v chevereto_config:/data -v $(pwd):/backup alpine tar xzf /backup/chevereto_config.tar.gz -C /data
docker run --rm -v chevereto_db:/data -v $(pwd):/backup alpine tar xzf /backup/chevereto_db.tar.gz -C /data
```