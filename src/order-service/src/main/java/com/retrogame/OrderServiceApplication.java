package com.retrogame.orderservice;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@SpringBootApplication
@RestController
public class OrderServiceApplication {

    private List<Map<String, Object>> orders = new ArrayList<>();
    private int orderIdCounter = 1;

    public static void main(String[] args) {
        SpringApplication.run(OrderServiceApplication.class, args);
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "healthy", "service", "order-service");
    }

    @GetMapping("/orders")
    public List<Map<String, Object>> getOrders() {
        return orders;
    }

    @GetMapping("/orders/{userId}")
    public List<Map<String, Object>> getUserOrders(@PathVariable String userId) {
        List<Map<String, Object>> userOrders = new ArrayList<>();
        for (Map<String, Object> order : orders) {
            if (order.get("userId").equals(userId)) {
                userOrders.add(order);
            }
        }
        return userOrders;
    }

    @PostMapping("/orders")
    public Map<String, Object> createOrder(@RequestBody Map<String, Object> orderRequest) {
        Map<String, Object> order = new HashMap<>();
        order.put("orderId", orderIdCounter++);
        order.put("userId", orderRequest.get("userId"));
        order.put("items", orderRequest.get("items"));
        order.put("total", orderRequest.get("total"));
        order.put("status", "PENDING");
        order.put("createdAt", new Date().toString());
        orders.add(order);
        return order;
    }

    @PutMapping("/orders/{orderId}/status")
    public Map<String, Object> updateOrderStatus(@PathVariable int orderId, @RequestBody Map<String, String> body) {
        for (Map<String, Object> order : orders) {
            if (order.get("orderId").equals(orderId)) {
                order.put("status", body.get("status"));
                return order;
            }
        }
        return Map.of("error", "Order not found");
    }
}