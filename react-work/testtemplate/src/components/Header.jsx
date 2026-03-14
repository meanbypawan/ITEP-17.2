import { Component } from "react";

class Header extends Component{
    render(){
        return <>
          
      <header className="header_section">
        <div className="container-fluid">
          <nav className="navbar navbar-expand-lg custom_nav-container">
            <a className="navbar-brand" href="index.html">
              <span>
                Healet
              </span>
            </a>
            <div className="" id="">

              <div className="custom_menu-btn">
                <button onclick="openNav()">
                  <span className="s-1"> </span>
                  <span className="s-2"> </span>
                  <span className="s-3"> </span>
                </button>
                <div id="myNav" className="overlay">
                  <div className="overlay-content">
                    <a href="index.html">Home</a>
                    <a href="about.html">About</a>
                    <a href="shop.html">Shop</a>
                    <a href="blog.html">Blog</a>
                  </div>
                </div>
              </div>

            </div>
          </nav>
        </div>
      </header>
        </>
    }
}

export default Header;