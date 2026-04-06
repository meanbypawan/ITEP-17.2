import { Link } from "react-router-dom";

function Header(){
    return <>
    <nav className="navbar navbar-expand-sm bg-light">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/product">Product</Link>
                </li>
            </ul>

        </nav>
    </>
}

export default Header;