import { Component } from "react";

class Footer extends Component{
    render(){
        return <>
          

      <section className="offer_section layout_padding">
        <div className="container-fluid">
          <div className="row">
            <div className="col-md-7 px-0">
              <div className="box offer-box1">
                <img src="images/o1.jpg" alt="" />
                <div className="detail-box">
                  <h2>
                    Upto 15% Off
                  </h2>
                  <a href="">
                    Shop Now
                  </a>
                </div>
              </div>
            </div>
            <div className="col-md-5 px-0">
              <div className="box offer-box2">
                <img src="images/o2.jpg" alt="" />
                <div className="detail-box">
                  <h2>
                    Upto 10% Off
                  </h2>
                  <a href="">
                    Shop Now
                  </a>
                </div>
              </div>
              <div className="box offer-box3">
                <img src="images/o3.jpg" alt="" />
                <div className="detail-box">
                  <h2>
                    Upto 20% Off
                  </h2>
                  <a href="">
                    Shop Now
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="blog_section ">
        <div className="container">
          <div className="heading_container">
            <h2>
              Latest From Blog
            </h2>
          </div>
          <div className="row">
            <div className="col-md-6">
              <div className="box">
                <div className="img-box">
                  <img src="images/b1.jpg" alt="" />
                  <h4 className="blog_date">
                    14 <br />
                    July
                  </h4>
                </div>
                <div className="detail-box">
                  <h5>
                    Molestiae ad reiciendis dignissimos
                  </h5>
                  <p>
                    alteration in some form, by injected humour, or randomised words which don't look even slightly believable.
                  </p>
                  <a href="">
                    Read More
                  </a>
                </div>
              </div>
            </div>
            <div className="col-md-6">
              <div className="box">
                <div className="img-box">
                  <img src="images/b2.jpg" alt="" />
                  <h4 className="blog_date">
                    15 <br />
                    July
                  </h4>
                </div>
                <div className="detail-box">
                  <h5>
                    Dolores vel maiores voluptatem enim
                  </h5>
                  <p>
                    alteration in some form, by injected humour, or randomised words which don't look even slightly believable.
                  </p>
                  <a href="">
                    Read More
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>


      <section className="client_section layout_padding">
        <div className="container">
          <div className="heading_container">
            <h2>
              Testimonial
            </h2>
          </div>
          <div id="carouselExample2Controls" className="carousel slide" data-ride="carousel">
            <div className="carousel-inner">
              <div className="carousel-item active">
                <div className="row">
                  <div className="col-md-11 col-lg-10 mx-auto">
                    <div className="box">
                      <div className="img-box">
                        <img src="images/client.jpg" alt="" />
                      </div>
                      <div className="detail-box">
                        <div className="name">
                          <h6>
                            Samantha Jonas
                          </h6>
                        </div>
                        <p>
                          It is a long established fact that a reader will be
                          distracted by the readable cIt is a long established fact
                          that a reader will be distracted by the readable c
                        </p>
                        <i className="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="carousel-item">
                <div className="row">
                  <div className="col-md-11 col-lg-10 mx-auto">
                    <div className="box">
                      <div className="img-box">
                        <img src="images/client.jpg" alt="" />
                      </div>
                      <div className="detail-box">
                        <div className="name">
                          <h6>
                            Samantha Jonas
                          </h6>
                        </div>
                        <p>
                          It is a long established fact that a reader will be
                          distracted by the readable cIt is a long established fact
                          that a reader will be distracted by the readable c
                        </p>
                        <i className="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="carousel-item">
                <div className="row">
                  <div className="col-md-11 col-lg-10 mx-auto">
                    <div className="box">
                      <div className="img-box">
                        <img src="images/client.jpg" alt="" />
                      </div>
                      <div className="detail-box">
                        <div className="name">
                          <h6>
                            Samantha Jonas
                          </h6>
                        </div>
                        <p>
                          It is a long established fact that a reader will be
                          distracted by the readable cIt is a long established fact
                          that a reader will be distracted by the readable c
                        </p>
                        <i className="fa fa-quote-left" aria-hidden="true"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="carousel_btn-container">
              <a className="carousel-control-prev" href="#carouselExample2Controls" role="button" data-slide="prev">
                <i className="fa fa-long-arrow-left" aria-hidden="true"></i>
                <span className="sr-only">Previous</span>
              </a>
              <a className="carousel-control-next" href="#carouselExample2Controls" role="button" data-slide="next">
                <i className="fa fa-long-arrow-right" aria-hidden="true"></i>
                <span className="sr-only">Next</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      <section className="info_section layout_padding2">
        <div className="container">
          <div className="row info_form_social_row">
            <div className="col-md-8 col-lg-9">
              <div className="info_form">
                <form action="">
                  <input type="email" placeholder="Enter your email" />
                  <button>
                    <i className="fa fa-arrow-right" aria-hidden="true"></i>
                  </button>
                </form>
              </div>
            </div>
            <div className="col-md-4 col-lg-3">

              <div className="social_box">
                <a href="">
                  <i className="fa fa-facebook" aria-hidden="true"></i>
                </a>
                <a href="">
                  <i className="fa fa-twitter" aria-hidden="true"></i>
                </a>
                <a href="">
                  <i className="fa fa-linkedin" aria-hidden="true"></i>
                </a>
              </div>
            </div>
          </div>
          <div className="row info_main_row">
            <div className="col-md-6 col-lg-3">
              <div className="info_links">
                <h4>
                  Menu
                </h4>
                <div className="info_links_menu">
                  <a href="index.html">Home</a>
                  <a href="about.html">About</a>
                  <a href="shop.html">Shop</a>
                  <a href="blog.html">Blog</a>
                </div>
              </div>
            </div>
            <div className="col-md-6 col-lg-3">
              <div className="info_insta">
                <h4>
                  Instagram
                </h4>
                <div className="insta_box">
                  <div className="img-box">
                    <img src="images/p1.png" alt="" />
                  </div>
                  <p>
                    long established fact that a reader
                  </p>
                </div>
                <div className="insta_box">
                  <div className="img-box">
                    <img src="images/p2.png" alt="" />
                  </div>
                  <p>
                    long established fact that a reader
                  </p>
                </div>
              </div>
            </div>
            <div className="col-md-6 col-lg-3">
              <div className="info_detail">
                <h4>
                  About Us
                </h4>
                <p className="mb-0">
                  when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to
                </p>
              </div>
            </div>
            <div className="col-md-6 col-lg-3">
              <h4>
                Contact Us
              </h4>
              <div className="info_contact">
                <a href="">
                  <i className="fa fa-map-marker" aria-hidden="true"></i>
                  <span>
                    Location
                  </span>
                </a>
                <a href="">
                  <i className="fa fa-phone" aria-hidden="true"></i>
                  <span>
                    Call +01 1234567890
                  </span>
                </a>
                <a href="">
                  <i className="fa fa-envelope"></i>
                  <span>
                    demo@gmail.com
                  </span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <footer className="footer_section">
        <div className="container">
          <p>
            &copy; <span id="displayYear"></span> All Rights Reserved By
            <a href="https://html.design/">Free Html Templates</a>
          </p>
        </div>
      </footer>
        </>
    }
}

export default Footer;