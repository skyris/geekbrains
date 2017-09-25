function Container() {
  this.id = "";
  this.className = "";
  this.htmlCode = "";
  this.nestedItems = [];
}

Container.prototype.render = function() {
  return this.htmlCode;
}

Container.prototype.addNestedItems = function(items) {
  for (var item of items) {
    this.nestedItems.push(item);
  }
}

Container.prototype.addAttrClass = function () {
  return this.className?" class='" + this.className + "' ":"";
}

Container.prototype.addAttrId = function () {
  return this.id?" id='" + this.id+ "' ":"";
}

Container.prototype.remove = function() {
  if (this.id) {
    document.getElementById(this.id).remove()
  } else {
      // Находим все элементы класса и в них ищем те которые имеют html, содержащий данные this.href и this.itemName 
      // Поскольку мы хотим удалить самый нижний узел в иерархии узлов, то ищем узел с минимальной длинной html
      // И удаляем его
      // Костыльно, но что-то с чего нужно начать
      var elems = document.getElementsByClassName(this.className);
      var regex = this.href + ".+?" + this.itemName; 
      html_length = Infinity;
      for(var elem of elems) {
        if(elem.innerHTML.match(regex)) {
          curr_html_length  = elem.innerHTML.length;
          if (curr_html_length < html_length) {
            curr_elem = elem
          }
        }
      }
      curr_elem.remove();
    }
} 

 

function Menu(my_id, my_class) {
  Container.call(this);
  this.id = my_id;
  this.className = my_class;
}


Menu.prototype = Object.create(Container.prototype);
Menu.prototype.constructor = Menu;
Menu.prototype.render = function() {
  var result = "<ul" + this.addAttrClass() + this.addAttrId() + ">";  
  for (var item of this.nestedItems) {
    if(item instanceof MenuItem) {
      result += item.render();
    }
  }
  result += "</ul>";
  return result;
}


function MenuItem(my_href, my_name) {
  Container.call(this);
  this.className = "menu_item";
  this.href = my_href;
  this.itemName  = my_name;
}

MenuItem.prototype = Object.create(Container.prototype);
MenuItem.prototype.constructor = MenuItem;
MenuItem.prototype.render = function() {
  if (this.nestedItems.length) {
    return "<li" + this.addAttrClass() + this.addAttrId() +  "><a href='" + this.href + "'>" + this.itemName + "</a><ul>" + 
             this.nestedItems.reduce(function(sum, current) {
                                        return sum + current.render();
                                     }, "") + "</ul></li>"
  } else {
      return "<li" + this.addAttrClass() + "><a href='" + this.href + "'>" + this.itemName + "</a></li>"
  }
}




var m_item1 = new MenuItem("/", "Главная");
var m_item2 = new MenuItem("/catalogue/", "Каталог");
var m_item3 = new MenuItem("/gallery/", "Галерея");
var m_items = [m_item1, m_item2, m_item3];

var m_item4 = new MenuItem("/", "Second level");
var m_item5 = new MenuItem("/catalogue/", "Second catalog");
var m_item6 = new MenuItem("/gallery/", "Second galery");

var m_item7 = new MenuItem("/", "Каталог 3");
var m_item8 = new MenuItem("/catalogue/", "Каталог 3");
var m_item9 = new MenuItem("/gallery/", "Галерея 3 сейчас будет удалена");

m_item1.addNestedItems([m_item4]);
m_item2.addNestedItems([m_item4, m_item5]);
m_item3.addNestedItems([m_item6]);

m_item6.addNestedItems([m_item7, m_item8, m_item9]);

var menu = new Menu("my_menu", "my_class");
menu.addNestedItems(m_items);


var div = document.write(menu.render());
setTimeout(function(){ m_item9.remove(); }, 3000);
