using Microsoft.AspNetCore.Mvc;

namespace PaymentService.Controllers;

[ApiController]
[Route("[controller]")]
public class PaymentController : ControllerBase
{
    private static List<Dictionary<string, object>> payments = new();
    private static int paymentIdCounter = 1;

    [HttpGet("/health")]
    public IActionResult Health()
    {
        return Ok(new { status = "healthy", service = "payment-service" });
    }

    [HttpGet("/payments")]
    public IActionResult GetPayments()
    {
        return Ok(payments);
    }

    [HttpPost("/payments")]
    public IActionResult ProcessPayment([FromBody] Dictionary<string, object> request)
    {
        var payment = new Dictionary<string, object>
        {
            { "paymentId", paymentIdCounter++ },
            { "orderId", request["orderId"] },
            { "userId", request["userId"] },
            { "amount", request["amount"] },
            { "status", "SUCCESS" },
            { "createdAt", DateTime.Now.ToString() }
        };
        payments.Add(payment);
        return Ok(payment);
    }

    [HttpGet("/payments/{userId}")]
    public IActionResult GetUserPayments(string userId)
    {
        var userPayments = payments.Where(p => p["userId"].ToString() == userId).ToList();
        return Ok(userPayments);
    }
}