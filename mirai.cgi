#!/Applications/xampp/xamppfiles/bin/perl -w
@message=("2012年の早々にはiPhone 5が発表されるだろう","君たちの時間は限られている。だから自分以外の他の誰かの人生を生きて無駄にする暇なんかない。","未来に先回りして点と点を繋げて見ることはできない、君たちにできるのは過去を振り返って繋げることだけなんだ。","ユッケを食べたいと思うことが時々よくあるよ","ソーシャルネットワークを通して国や宗教を超えた１つのレイヤーが世界に生まれつつある、そこに企業がどう関わりどうリードしていくか、今後数年間でさらにダイナミズムに世界が変わるだろう","Perlは無くならないよ、永遠に","グルーポンでおせちでも買うのかい？","全てのコンピューターからマウスとキーボードが無くなる日がくるだろう");
print "Content-Type: text/html;charset=utf8\n\n";
print "<html><head><title>iSteace for Perl</title></head>";
print "<body>";
print "Webの未来を聞いてみる<br>\n";
print "<h1>「@message[rand 8]」</h1>";
print "Twitterに<a href=\"http://twitter.com\" target=\"_bank\"
>つぶやく</a>（つぶやく方法はCtrl + Cでコピー、Twitterの入力画面でCtrl + Vを押せば大丈夫です)";
__END__;;