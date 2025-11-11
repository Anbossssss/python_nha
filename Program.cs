using CodeHollow.FeedReader;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/rss", async (HttpContext ctx) =>
{
    string? url = ctx.Request.Query["url"];
    if (string.IsNullOrEmpty(url))
        return Results.BadRequest("Thiếu tham số url");

    try
    {
        var feed = await FeedReader.ReadAsync(url);
        var items = feed.Items.Take(20).Select(it => new
        {
            title = it.Title,
            link = it.Link,
            summary = it.Description,
            published = it.PublishingDateString
        });

        return Results.Json(items);
    }
    catch (Exception ex)
    {
        return Results.Problem(ex.Message);
    }
});

app.MapGet("/", () => Results.Text(@"
<!doctype html>
<html lang='vi'>
<head>
  <meta charset='utf-8'>
  <title>Đọc báo ASP.NET</title>
  <style>
    body { font-family: Arial, sans-serif; margin:0; padding:0; }
    header { background:#0078d7; color:white; padding:10px; }
    input, button { padding:6px; font-size:14px; }
    main { display:flex; height:90vh; }
    #list { width:30%; border-right:1px solid #ccc; margin:0; padding:0; overflow-y:auto; }
    #list li { list-style:none; padding:10px; border-bottom:1px solid #eee; cursor:pointer; }
    #list li:hover { background:#f0f0f0; }
    #viewer { flex:1; padding:20px; overflow-y:auto; }
    #viewer h2 { margin-top:0; }
    #viewer small { color:#666; }
  </style>
</head>
<body>
  <header>
    <h1>📰 Đọc báo ASP.NET Core</h1>
    <input id='rss' size='60' value='https://vnexpress.net/rss/tin-moi-nhat.rss'/>
    <button onclick='load()'>Tải tin</button>
  </header>
  <main>
    <ul id='list'></ul>
    <div id='viewer'><em>Chọn một bài báo để đọc...</em></div>
  </main>

<script>
async function load(){
  let url = document.getElementById('rss').value;
  let res = await fetch('/rss?url='+encodeURIComponent(url));
  let items = await res.json();
  let list = document.getElementById('list'); list.innerHTML='';
  let viewer = document.getElementById('viewer'); viewer.innerHTML='<em>Chọn một bài báo để đọc...</em>';
  
  items.forEach((it,i)=>{
    let li=document.createElement('li');
    li.textContent = it.title;
    li.onclick=()=>{
      viewer.innerHTML = `
        <h2>${it.title}</h2>
        <small>${it.published || ''}</small>
        <div>${it.summary || 'Không có tóm tắt'}</div>
        <p><a href='${it.link}' target='_blank'>Đọc bản đầy đủ</a></p>
      `;
    };
    list.appendChild(li);

    if(i==0) { // tự động mở bài đầu tiên
      viewer.innerHTML = `
        <h2>${it.title}</h2>
        <small>${it.published || ''}</small>
        <div>${it.summary || 'Không có tóm tắt'}</div>
        <p><a href='${it.link}' target='_blank'>Đọc bản đầy đủ</a></p>
      `;
    }
  });
}
</script>
</body>
</html>
", "text/html"));

app.Run();
