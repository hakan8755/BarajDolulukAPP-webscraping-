Baraj Doluluk Tahmini Projesi

Bu proje, çeşitli meteorolojik ve tüketim verilerini kullanarak baraj doluluk oranlarını tahmin etmeyi amaçlamaktadır. Proje kapsamında veriler, Selenium kutuphanesi ile internet üzerinden toplanmakta olup baraj doluluk seviyesinin tahmini icin kullanılacaktır. Dosyaların işlevleri aşağıda detaylandırılmıştır.

Proje Yapısı

denizbasıncı.py: Deniz seviyesindeki basınç verilerini toplamak ve işlemek için kullanılır.

dewpoint.py: Toplanan meteorolojik verilere dayanarak çiy noktası hesaplamaları yapar.

from_selenium_import.py: Selenium tabanlı veri çekimi için gerekli kütüphane ve fonksiyonları içerir.

ibblçetüketim.py: İstanbul Büyükşehir Belediyesi’nden su tüketim verilerini toplar.

ibbselenium.py: İstanbul veri portalı için Selenium yapılandırmaları ve fonksiyonlarını içerir.

ilcetuketim2015ekadar.py: 2015 yılına kadar olan ilçe bazında su tüketim verilerini içerir.

iskibarajaduşenyağmur.py: Baraj seviyelerini etkileyen yağış oranı verilerini toplar.

rüzgarhızı.py: Buharlaşma oranlarını etkileyebilecek rüzgar hızını toplamak için kullanılır.


Veri Toplama
 Selenium aracı kullanılarak toplanmaktadır. Bu veriler deniz basıncı, çiy noktası, rüzgar hızı, yağış miktarı ve tarihsel su tüketim verilerini içermektedir.
