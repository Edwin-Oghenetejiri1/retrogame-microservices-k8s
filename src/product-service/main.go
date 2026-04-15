package main

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"
)

type Product struct {
	ID       int     `json:"id"`
	Name     string  `json:"name"`
	Category string  `json:"category"`
	Price    float64 `json:"price"`
	Stock    int     `json:"stock"`
	Image    string  `json:"image"`
}

var products = []Product{
	{ID: 1, Name: "Nintendo Entertainment System", Category: "Console", Price: 150.00, Stock: 10, Image: "nes.jpg"},
	{ID: 2, Name: "Sega Genesis", Category: "Console", Price: 120.00, Stock: 8, Image: "sega.jpg"},
	{ID: 3, Name: "Super Nintendo", Category: "Console", Price: 180.00, Stock: 5, Image: "snes.jpg"},
	{ID: 4, Name: "Atari 2600", Category: "Console", Price: 90.00, Stock: 12, Image: "atari.jpg"},
	{ID: 5, Name: "Super Mario Bros", Category: "Game", Price: 25.00, Stock: 20, Image: "mario.jpg"},
	{ID: 6, Name: "Sonic the Hedgehog", Category: "Game", Price: 20.00, Stock: 15, Image: "sonic.jpg"},
	{ID: 7, Name: "The Legend of Zelda", Category: "Game", Price: 30.00, Stock: 10, Image: "zelda.jpg"},
	{ID: 8, Name: "Street Fighter II", Category: "Game", Price: 22.00, Stock: 18, Image: "sf2.jpg"},
}

func setHeaders(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
}

func getProducts(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)
	_ = json.NewEncoder(w).Encode(products)
}

func getProduct(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)

	idStr := r.URL.Query().Get("id")
	if idStr == "" {
		http.Error(w, "missing id parameter", http.StatusBadRequest)
		return
	}

	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "invalid id format", http.StatusBadRequest)
		return
	}

	for _, p := range products {
		if p.ID == id {
			_ = json.NewEncoder(w).Encode(p)
			return
		}
	}

	http.Error(w, "product not found", http.StatusNotFound)
}

func deleteProduct(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)

	idStr := r.URL.Query().Get("id")
	if idStr == "" {
		http.Error(w, "missing id parameter", http.StatusBadRequest)
		return
	}

	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "invalid id format", http.StatusBadRequest)
		return
	}

	for i, p := range products {
		if p.ID == id {
			products = append(products[:i], products[i+1:]...)
			_ = json.NewEncoder(w).Encode(map[string]string{
				"message": "product deleted",
			})
			return
		}
	}

	http.Error(w, "product not found", http.StatusNotFound)
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
	setHeaders(w)
	_ = json.NewEncoder(w).Encode(map[string]string{
		"status":  "healthy",
		"service": "product-service",
	})
}

func main() {
	http.HandleFunc("/products", getProducts)
	http.HandleFunc("/product", getProduct)
	http.HandleFunc("/product/delete", deleteProduct)
	http.HandleFunc("/health", healthCheck)

	log.Println("Product service starting on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
















