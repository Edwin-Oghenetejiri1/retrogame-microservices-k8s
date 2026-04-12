# Build stage
FROM maven:3.9.6-eclipse-temurin-21 AS BUILD

WORKDIR /app

COPY pom.xml ./

RUN mvn dependency:go-offline

COPY src ./src

RUN mvn package -DskipTests

# Run stage
FROM eclipse-temurin:21-jre-alpine AS RELEASE

WORKDIR /app

COPY --from=BUILD /app/target/*.jar app.jar

EXPOSE 8082

CMD ["java", "-jar", "app.jar"]
