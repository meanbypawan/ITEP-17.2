import { Link, Outlet } from "react-router-dom";

function Product(){
    console.log("Product render...");
    return <>
      <div className="container mt-2">
        <h1>Product Component...</h1>
        <Link to="discounted-product"><button className="btn btn-success">Discounted product</button></Link>
        <Link to="feature-product"><button className="btn btn-primary ml-3">Feature product</button></Link>
      </div>
      <div className="container mt-3">
        <p>dfslkf fdslkfjdf fdslfkjdsreio Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit blanditiis ex aut dicta ullam laboriosam quod et nobis praesentium distinctio. Corporis ipsum adipisci laudantium eligendi perferendis possimus architecto voluptatibus incidunt quas deleniti, quasi ex praesentium odit ratione, accusantium, minus fugit exercitationem hic numquam deserunt omnis? Consequatur quam repellendus ipsa voluptas, libero enim beatae dolorem, veritatis facilis velit delectus soluta eligendi sint! Qui officiis inventore aspernatur. Perspiciatis ad, nostrum quam, quasi earum voluptate doloremque, aut dolorem placeat asperiores eius recusandae veritatis. Odit dolore repudiandae sint, harum odio veritatis quod dolorum beatae hic deserunt eligendi officiis dicta, adipisci tenetur sit? Doloremque, voluptatem?</p>
        <hr/>
        <Outlet/>
      </div>
    </>
}
export default Product;