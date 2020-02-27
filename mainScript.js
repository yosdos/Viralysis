var ViralysisB1 = document.cookie.indexOf('ViralysisId=');
var ViralysisE1 = document.cookie.indexOf(';', ViralysisB1+12);
if (ViralysisE1 == -1) ViralysisE1 = document.cookie.length;
if (ViralysisB1 == -1) var ViralysisId = "";
else var ViralysisId = document.cookie.substring(ViralysisB1+12, ViralysisE1);
var ViralysisB2 = window.location.hash.indexOf('&vai=');
if (ViralysisB2 == -1) var vai = "";
else var vai = window.location.hash.substring(ViralysisB2+5, ViralysisB2+11);
try{
var ViralysisUrl = "https://1asdd2nwvf.execute-api.us-east-1.amazonaws.com/CommunityAndViralityAnalysis";
var ViralysisXmlhttp = new XMLHttpRequest();
ViralysisXmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       var resp = JSON.parse(this.responseText);
       if (ViralysisB2 == -1) window.location.hash = window.location.hash + "#&vai=" + resp.vai;
       else window.location.hash = window.location.hash.replace(vai,resp.vai);
       document.cookie = "ViralysisId="+resp.ViralysisId+"; Max-Age=50000000; Domain="+window.location.hostname;}};
ViralysisXmlhttp.open("POST", ViralysisUrl, true);
ViralysisXmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
ViralysisXmlhttp.withCredentials = true;
ViralysisXmlhttp.send(JSON.stringify({"ViralysisId":ViralysisId,"vai":vai,"href":window.location.href, "ViralysisClientId":"Insert Your name user", "referrer":document.referrer})); }catch(err) {}
