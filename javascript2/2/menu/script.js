function Container() {
  this.id = "";
  this.className = "";
  this.htmlCode = "";
  this.nestedItems = [];
}

Container.prototype.addNestedItems = function(items) {
    console.log(items);
  for (var item of items) {
    this.nestedItems.push(item);
  }
}

Container.prototype.render = function () {
    return this.htmlCode;
}
Container.prototype.addIdAndClass = function () {
    return (this.id?" id='" + this.id + "'": "") + (this.className?" class='" + this.className + "'": "");
}

// ------------------- Menu ----------------------

function Menu(my_id, my_class) {
  Container.call(this);
  this.id = my_id;
  this.className = my_class;
}

Menu.prototype = Object.create(Container.prototype);
Menu.prototype.constructor = Menu;
Menu.prototype.render = function() {
  var result = "<div" + this.addIdAndClass() + "><ul>";
  for (var item of this.nestedItems) {
    if(item instanceof MenuItem) {
      result += item.render();
    }
  }
  result += "</ul></div>";
  return result;
}



// ------------------- MenuItem ----------------------

function MenuItem(my_href, my_name) {
    Container.call(this);
    this.href = my_href;
    this.itemName = my_name;

    var parentMethod = this.addNestedItems;
    this.addNestedItems = function (items) {
        parentMethod.call(this, items);
        this.className = "parent";
    }
}

MenuItem.prototype = Object.create(Container.prototype);
MenuItem.prototype.constructor = MenuItem;
MenuItem.prototype.render = function() {
  if (this.nestedItems.length) {
    return "<li" + this.addIdAndClass() +  "><a href='" + this.href + "'>" + this.itemName + "</a><ul>" +
             this.nestedItems.reduce(function(sum, current) {
                                        return sum + current.render();
                                     }, "") + "</ul></li>"
  } else {
      return "<li" + this.addIdAndClass() + "><a href='" + this.href + "'>" + this.itemName + "</a></li>"
  }
}

var menu = new Menu("mainmenu", "");

var m_item1 = new MenuItem("#", "Личный кабинет");
var m_item2 = new MenuItem("#", "Каталог");
var m_item3 = new MenuItem("#", "Промоакции");

var m_item4 = new MenuItem("#", "Ноутбуки и планшены");
var m_item5 = new MenuItem("#", "Компьютеры и периферия");
var m_item6 = new MenuItem("#", "Комплектующие для ПК");
var m_item7 = new MenuItem("#", "Телефоны и смарт часы");
var m_item8 = new MenuItem("#", "Фото-ведеоаппаратура");

var m_item9 = new MenuItem("#", "Ноутбуки");
var m_item11 = new MenuItem("#", "Планшены");
var m_item12 = new MenuItem("#", "Android");
var m_item13 = new MenuItem("#", "iPhone");
var m_item14 = new MenuItem("#", "Смарт часы");

menu.addNestedItems([m_item1, m_item2, m_item3]);
m_item2.addNestedItems([m_item4, m_item5, m_item6, m_item7, m_item8]);

m_item4.addNestedItems([m_item9, m_item11]);
m_item7.addNestedItems([m_item12, m_item13, m_item14]);

var div = document.write(menu.render());
