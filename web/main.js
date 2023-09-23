async function command() {
    var e1 = document.getElementById("country");
    var country = e1.options[e1.selectedIndex].text;

    var e2 = document.getElementById("language");
    var language = e2.options[e2.selectedIndex].text;

    let Result = await eel.get_actual_news(country, language)();
    document.getElementById('Result').innerHTML = Result;
}

$('#command').click(function(){
   command();
})