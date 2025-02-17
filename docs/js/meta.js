let metaTags = `
  <meta property="og:title" content="${document.title}">
  <meta property="og:description" content="这是lyy19的个人博客网站，欢迎访问并在留言板留言。网站使用GitHub作为图床。">
  <meta property="og:image" content="https://raw.githubusercontent.com/lyy1119/Imgs/main/img/1709210261156.png">
  <meta property="og:url" content="${window.location.href}">
  <meta property="og:type" content="website">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="lyy19's blog">
  <meta name="twitter:description" content="这是lyy19的个人博客网站，欢迎访问并在留言板留言。网站使用GitHub作为图床。">
  <meta name="twitter:image" content="https://raw.githubusercontent.com/lyy1119/Imgs/main/img/1709210261156.png">

`;
document.head.innerHTML += metaTags;
