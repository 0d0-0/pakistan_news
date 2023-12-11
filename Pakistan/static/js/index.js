const carouselItems = document.querySelectorAll(".carousel-item");
let currentItem = 0;
setInterval(() => {
    if (currentItem >= carouselItems.length - 1) {
        currentItem = 0;
    } else {
        currentItem++;
    }
    carouselItems.forEach((item) => {
        item.classList.remove("active");
    });
    carouselItems[currentItem].classList.add("active");
}, 3000);
function showDiv(divNumber) {
    var div1 = document.getElementById('div1');
    var div2 = document.getElementById('div2');
    var div3 = document.getElementById('div3');

    if (divNumber === 1) {
        div1.style.display = 'block';
        div2.style.display = 'none';
        div3.style.display = 'none';
    }
    else if (divNumber === 2) {
        div1.style.display = 'none';
        div2.style.display = 'block';
        div3.style.display = 'none';
    }
    else if (divNumber === 3) {
        div1.style.display = 'none';
        div2.style.display = 'none';
        div3.style.display = 'block';
    }
}
function toggleDiv() {
  var myDiv = document.getElementById("myDiv");
  if (myDiv.style.display === "none") {
    myDiv.style.display = "block";
  } else {
    myDiv.style.display = "none";
  }
}
function hideDiv2() {
    var myDiv2 = document.getElementById("myDiv2");
    myDiv2.style.display = "none";
}
function showDiv2() {
    var myDiv2 = document.getElementById("myDiv2");
    myDiv2.style.display = "block";
}
var markers = [];

function addMarker(latitude, longitude) {
    // 清除所有旧标记
    for (var i = 0; i < markers.length; i++) {
        map.removeOverlay(markers[i]);
    }
    // 添加新标记
    var marker = new BMap.Marker(new BMap.Point(longitude, latitude));
    map.addOverlay(marker);
    map.panTo(new BMap.Point(longitude, latitude));
    // 将新标记添加到标记数组中
    markers.push(marker);
}
function showFloatingWindow() {
    var floatingWindow = document.getElementById("floatingWindow");
    floatingWindow.style.display = "block";
}

function hideFloatingWindow() {
    var floatingWindow = document.getElementById("floatingWindow");
    floatingWindow.style.display = "none";
}
function disFunction(event) {
    event.preventDefault(); // 阻止默认行为
    // 其他操作代码
}
function showPakistanTime() {
    const timeZoneOffset = 5 * 60; // 巴基斯坦比UTC时间快5个小时
    const pakistanTime = new Date(new Date().getTime() + timeZoneOffset * 60 * 1000);
    const hour = pakistanTime.getHours();
    const minute = pakistanTime.getMinutes();
    const second = pakistanTime.getSeconds();
    let suffix = "am";
    let hour12 = hour;
    if (hour >= 12) {
      hour12 = hour - 12;
      suffix = "pm";
    }
    if (hour12 === 0) {
      hour12 = 12;  // 特殊情况，0时表示12点
    }
    document.getElementById("PakistanTime").innerHTML =
      `${hour12}:${minute}:${second} ${suffix}`;
  }

  // 每秒更新一次时间
  setInterval(showPakistanTime, 1000);