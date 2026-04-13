const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const PRODUCT_SERVICE = 'http://product-service:8080';
const CART_SERVICE = 'http://cart-service:8081';
const ORDER_SERVICE = 'http://order-service:8082';

// Home page - show all products
app.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${PRODUCT_SERVICE}/products`);
        res.render('index', { products: response.data });
    } catch (error) {
        res.render('index', { products: [] });
    }
});

// Get cart
app.get('/cart/:userId', async (req, res) => {
    try {
        const response = await axios.get(`${CART_SERVICE}/cart/${req.params.userId}`);
        res.render('cart', { cart: response.data });
    } catch (error) {
        res.render('cart', { cart: { items: [] } });
    }
});

// Add to cart
app.post('/cart/:userId/add', async (req, res) => {
    try {
        await axios.post(`${CART_SERVICE}/cart/${req.params.userId}/add`, req.body);
        res.redirect(`/cart/${req.params.userId}`);
    } catch (error) {
        res.redirect('/');
    }
});

// Delete product
app.post('/product/delete', async (req, res) => {
    try {
        await axios.delete(`${PRODUCT_SERVICE}/product/delete?id=${req.body.id}`);
        res.redirect('/');
    } catch (error) {
        res.redirect('/');
    }
});

// Remove from cart
app.post('/cart/:userId/remove', async (req, res) => {
    try {
        await axios.delete(`${CART_SERVICE}/cart/${req.params.userId}/remove`, {
            data: { id: parseInt(req.body.id) }
        });
        res.redirect(`/cart/${req.params.userId}`);
    } catch (error) {
        res.redirect(`/cart/${req.params.userId}`);
    }
});

app.listen(3000, () => {
    console.log('Frontend service starting on port 3000...');
});