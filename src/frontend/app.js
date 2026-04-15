const express = require('express');
const axios = require('axios');
const path = require('node:path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const PRODUCT_SERVICE = 'http://product-service:8080';
const CART_SERVICE = 'http://cart-service:8081';

// Home
app.get('/', async (req, res) => {
    try {
        const response = await axios.get(`${PRODUCT_SERVICE}/products`);
        return res.render('index', { products: response.data });
    } catch (error) {
        console.error("Failed to load products:", error.message);
        return res.render('index', { products: [] });
    }
});

// Cart
app.get('/cart/:userId', async (req, res) => {
    try {
        const userId = Number.parseInt(req.params.userId, 10);

        if (Number.isNaN(userId)) {
            return res.status(400).send("Invalid user ID");
        }

        const response = await axios.get(`${CART_SERVICE}/cart/${userId}`);
        return res.render('cart', { cart: response.data });

    } catch (error) {
        console.error("Cart error:", error.message);
        return res.status(500).send("Internal server error");
    }
});

// Delete product
app.post('/product/delete', async (req, res) => {
    try {
        const id = Number.parseInt(req.body.id, 10);

        if (Number.isNaN(id)) {
            return res.redirect('/');
        }

        await axios.delete(`${PRODUCT_SERVICE}/product/delete`, {
            params: { id }
        });

        return res.redirect('/');
    } catch (error) {
        console.error("Delete error:", error.message);
        return res.redirect('/');
    }
});

app.listen(3000, () => {
    console.log('Frontend running on port 3000');
});