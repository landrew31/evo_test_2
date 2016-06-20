from bs4 import BeautifulSoup
import urllib2

from app import db
from models import Adjective

URL = 'http://dict.ruslang.ru/magn.php?act=list&list=%CF%F0%E8%EB%E0%E3%E0%F2%E5%EB%FC%ED%EE%E5'
page = urllib2.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')

epithets = []

for a in soup.find_all('td')[1].find_all('a')[6:]:
	epithets.append(a.get_text())

for epithet in epithets:
	if db.session.query(Adjective.adj).filter_by(adj=epithet).scalar() is None:
		one = Adjective(epithet)
		db.session.add(one)
		db.session.commit()