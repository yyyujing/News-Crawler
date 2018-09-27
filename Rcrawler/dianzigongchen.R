library("rvest")
library(stringr)
library(magrittr)
url <- "http://www.eeworld.com.cn/gykz/zhzx/" #电子工程网
web <- read_html(url)

#提取htmLnodes
news1 <- web%>%html_nodes("div.chan_toptxt")%>%html_nodes("a") #注意这里有两级类名的，可以直接用第一类的 
#提取新闻标题存入title
title1<- news1%>%html_text()
#提取网页的url存入link
link1 <- news1%>%html_attr("href")


#提取htmLnodes
news2 <- web%>%html_nodes("dt.tit")%>%html_nodes("a") #注意这里有两级类名的，可以直接用第一类的 
#提取新闻标题存入title
title2<- news2%>%html_text()
#提取网页的url存入link
link2 <- news2%>%html_attr("href")

#提取htmLnodes
news3 <- web%>%html_nodes("div.newspdail.boxm4")%>%html_nodes("a") #注意这里有两级类名的，可以直接用第一类的 
#提取新闻标题存入title
title3<- news3%>%html_text()
#提取网页的url存入link
link3 <- news3%>%html_attr("href")

title<-title1%>%append(title2)%>%append(title3)
link<-link1%>%append(link2)%>%append(link3)


article <- c(1:length(link))
article[]<-""

for(i in 1:length(link)) #抓取所有提取的新闻的内容
{
  x<-try(read_html(link[i]),silent = TRUE)
  if("try-error" %in% class(x))  next  #捕获异常并跳过此次循环，注意这里不用else 
  web<-read_html(link[i]) 
  article_nodes<-web%>%html_nodes("div.newscontxt p")  
  paras<-article_nodes%>%html_text()  
  article[i]<-paste(paras[1:length(paras)],collapse = "")
  print(i)
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
write.csv(newsdata,file = "newsdianzigongchen.csv",fileEncoding = "UTF-8",row.names = FALSE)