# coding=utf-8
from bs4 import BeautifulSoup

#HTML源码
html = """
<html>
	<head>
		<title>BeautifulSoup技术</title>
	</head>
	<body>
	<p class="title"><b>静夜思</b></p>
	<p class="content">
		窗前明月光，<br />
		疑似地上霜。 <br />
		举头望明月，<br />
		低头思故乡。 <br />
	</p>
	<p class="other">
		李白（701年－762年），字太白，号青莲居士，又号“谪仙人”，
		唐代伟大的浪漫主义诗人，被后人誉为“诗仙”，与
		<a href="http://example.com/dufu" class="poet" id="link1">杜甫</a>
		并称为“李杜”，为了与另两位诗人
		<a href="http://example.com/lishangyin" class="poet" id="link2">李商隐</a>、
		<a href="http://example.com/dumu" class="poet" id="link3">杜牧</a>即“小李杜”区别，杜甫与李白又合称“大李杜”。
		其人爽朗大方，爱饮酒...
	</p>
	<p class="story">...</p>
"""

#按照标准的缩进格式的结构输出
soup = BeautifulSoup(html)
print(soup.prettify())
