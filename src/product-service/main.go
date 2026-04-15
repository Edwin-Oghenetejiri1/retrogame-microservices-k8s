package main

import (
	"encoding/json"
	"fmt"
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

func getProducts(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(products)
}

func getProduct(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	id := r.URL.Query().Get("id")
	for _, p := range products {
		if fmt.Sprintf("%d", p.ID) == id {
			json.NewEncoder(w).Encode(p)
			return
		}
	}
	http.Error(w, "Product not found", http.StatusNotFound)
}

func healthCheck(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "healthy", "service": "product-service"})
}

func main() {
	http.HandleFunc("/products", getProducts)
	http.HandleFunc("/product", getProduct)
	http.HandleFunc("/product/delete", deleteProduct)
	http.HandleFunc("/health", healthCheck)

	log.Println("Product service starting on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func deleteProduct(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	idStr := r.URL.Query().Get("id")
	id, _ := strconv.Atoi(idStr)
	for i, p := range products {
		if p.ID == id {
			products = append(products[:i], products[i+1:]...)
			json.NewEncoder(w).Encode(map[string]string{"message": "Product deleted"})
			return
		}
	}
	http.Error(w, "Product not found", http.StatusNotFound)
}



