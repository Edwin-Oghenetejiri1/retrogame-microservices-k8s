# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS BUILD

WORKDIR /app

COPY *.csproj ./

RUN dotnet restore

COPY . .

RUN dotnet publish -c Release -o publish

# Run stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS RELEASE

WORKDIR /app

COPY --from=BUILD /app/publish .

EXPOSE 8083

CMD ["dotnet", "payment-service.dll"]