from icrawler.builtin import GoogleImageCrawler

attractionList = ['박수홍','George Clooney','Matt Damon','Sylvester Stallone','마동석','강호동','전현무','김흥국','하정우','이정재','박시후','이병헌','조인성','유승준','유아인','장동건',
                  'Tom Cruise','Chris Hemsworth','Tom Hiddleston','Will Smith', '배용준','정지훈','송중기','송강호','이병철','주원','이동욱','Takeshi Kitano','Keanu Reeves','Brad Pitt',
                  'Sean Connery','Daniel Craig','소지섭','정우성','차인표','강동원','원빈','이준기','황정민','유재석','유민상','김병만','김준현','박성호','정형돈','장동민','김구라','김국진',
                  '허각','박성광','로버트 할리','백종원', 'Robert Downey Jr', 'Benedict Cumberbatch', 'Chris Pratt', 'Mark Ruffalo', 'Tom Holland', '허경영', '이승기', '김수로', '김무열',
                  '공유', '정우성', '강다니엘', '지드래곤',
                  '수지', '홍진영', 'Chloe Moretz', '고현정', '한예슬', 'Scarlett Johansson', '한혜진', '박나래', '김태희', '전지현', '한지민', '신혜선', 'Hashimoto Kanna','Fan Bingbing',
                  'Emma Watson', '송지효', '백지영','라미란', '문소리', '아이유', '김혜수', '장나라', '문근영', '김연아', '박보영', '설리', '장윤정', '하지원', '김고은', '유인나', '김향기',
                  'Jodie Foster', '한지민', 'Liu Yan', 'Léa Seydoux', '오나미', '신봉선', '신보라','김신영', '이국주', '조혜련', '이영자', '곽현화', '박보미', '홍현희', '강수지', '안지영',
                  '서현', '오연서', '태연', '송혜교', '신아영', '김태리', '소유', '벤', '정유미', '신세경']
for keyword in attractionList:
    google_crawler = GoogleImageCrawler(parser_threads=1, downloader_threads=1, storage={'root_dir': 'images/{}'.format(keyword)})
    google_crawler.crawl(keyword=keyword, max_num=150, min_size=(500,500))



