library("rvest")
library(stringr)
library(magrittr)
url <- "http://www.chyxx.com/news/" #产业信息网
web <- read_html(url,encoding = 'gbk')

#提取htmLnodes
news <- web%>%html_nodes("div.hotnews")%>%html_nodes("ul.list")%>%html_nodes("a") #注意这里有两级类名的，可以直接用第一类的 
#提取新闻标题存入title
title<- news%>%html_text()
#提取网页的url存入link
link <- news%>%html_attr("href")


for(i in 1:length(link)){
  if( str_detect(link[i],"http")==FALSE)
    link[i]<-str_c("http://www.chyxx.com",link[i])
}


article <- c(1:length(link))
article[]<-""

for(i in 1:length(link)) #抓取所有提取的新闻的内容
{
  x<-try(read_html(link[i]),silent = TRUE)
  if("try-error" %in% class(x))  next  #捕获异常并跳过此次循环，注意这里不用else 
  web<-read_html(link[i]) 
  article_nodes<-web%>%html_nodes("div.articleBody p")  
  paras<-article_nodes%>%html_text()  
  article[i]<-paste(paras[1:length(paras)],collapse = "")
  
}


artempty<-str_detect(article,"") #这里是要删除为空值的文章

for(i in 1:length(artempty)){
  if (artempty[i]== FALSE ){
    link[i]<-NA
    title[i]<-NA
    article[i]<-NA
  }
}

link<-na.omit(link)
title<-na.omit(title)
article<-na.omit(article)


artempty<-str_detect(article,"NA") #删掉为NA的文章

for(i in 1:length(artempty)){
  if (artempty[i]== TRUE ){
    link[i]<-NA
    title[i]<-NA
    article[i]<-NA
  }
}

link<-na.omit(link)
title<-na.omit(title)
article<-na.omit(article)



newsdata<-data.frame(link=link,title=title,article=article)
write.csv(newsdata,file = "newschanyexinxi.csv",fileEncoding = "UTF-8",row.names = FALSE)
