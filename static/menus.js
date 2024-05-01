const MenuExpanders = document.querySelectorAll(".expanded-menu")

for(let menuItem of MenuExpanders) {

    if (sessionStorage.getItem(menuItem.id) == 1) {
        menuItem.classList += "expanded-menu--active"

    } else {
      sessionStorage.setItem(menuItem.id, 0)
    }

    clickable = document.getElementById(menuItem.id+"-click")

    clickable.addEventListener("click", () => {
      changeStateMenu(menuItem)
      var childrens = submenu.querySelectorAll(".expanded-menu--active")

      if (childrens) {
        for (let child of childrens) {

          currentState = sessionStorage.getItem(child.id)
          submenu = document.getElementById(child.id+"-submenu")
          arrow = document.getElementById(child.id+"-arrow")

          if (currentState == 1) {
                  child.classList.remove("expanded-menu--active")
                  submenu.classList.remove('submenu--active')
                  arrow.classList.remove('open-menu--active')
                  sessionStorage.setItem(child.id, 0)
          }
        }
      }
    })
}


function changeStateMenu(item) {
  currentState = sessionStorage.getItem(item.id)
  submenu = document.getElementById(item.id+"-submenu")
  arrow = document.getElementById(item.id+"-arrow")

  if (currentState == 1) {
          item.classList.remove("expanded-menu--active")
          submenu.classList.remove('submenu--active')
          arrow.classList.remove('open-menu--active')
          sessionStorage.setItem(item.id, 0)

  } else {
          arrow.classList.add('open-menu--active')
          item.classList += " expanded-menu--active"
          submenu.classList.add("submenu--active")
          sessionStorage.setItem(item.id, 1)
      }
}
