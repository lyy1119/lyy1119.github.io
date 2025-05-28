# Dockerfile在打包时编译

## 情境

对于某些项目，如`vue`、`Java`等构建的项目，可能项目过于庞大，对用户来说，自己搭建比较麻烦，尤其是这些项目的环境搭建及编译等对于经验不足的开发者和新手比较困难。  

对于这种问题，可以使用docker image提供的环境对项目先进行编译，再将编译好的文件用`COPY`复制到构建image的目录。  

## Dockerfile基本结构


这里用Vue编译静态文件，部署到Nginx做示范
```dockerfile
# Stage 1: 编译 Vue 应用
FROM node:18 AS build

WORKDIR /app
COPY ./frontend /app
RUN npm install && npm run build

# Stage 2: 用 Nginx 托管静态文件
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
```