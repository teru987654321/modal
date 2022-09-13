// modal-openクラスをクリックした時にモーダルウィンドウを表示する
$(".modal-open").modaal({
    overlay_close:true,//モーダル背景クリック時に閉じる
    hide_close: false, //閉じるボタンを表示
    before_open:function(){// モーダルが開く前に行う動作
        $('html').css('overflow-y','hidden');/*縦スクロールバーを出さない*/
    },
    after_close:function(){// モーダルが閉じた後に行う動作
        $('html').css('overflow-y','scroll');/*縦スクロールバーを出す*/
    }
});

// modal-closeクラスをクリックした時にモーダルウィンドウを閉じる
$('.modal-close').click(function(){
    $('.modal-open').modaal('close') 
});