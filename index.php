<link rel="stylesheet" href="home.css">


<?php
require_once('config.php');
// パスワードを設定する
$password = PS_WD;

// パスワードが正しく入力されていたらセッションを持たせる
if(isset($_POST['pass']) && $_POST['pass'] == $password){
    $_SESSION['login_ok'] = TRUE;
}

// セッションを持っていたらコンテンツを表示する
if(isset($_SESSION['login_ok'])){
  echo '<div class=main>';
	echo 'ログイン成功';
  echo '<a href="35.81.113.142">pleasanter</a>';
  echo '</div>';

}else{
  echo '<div class=main>';
	echo '<p>パスワードを入力してください</p>';
	echo '<form method="post">';
	echo '<input type="password" name="pass" class="box"><input type="submit" class="button" value="  ">';
	echo '</form>';
  echo '</div>';
}

?>
