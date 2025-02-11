package main

import (
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var DB *gorm.DB

func ConnectDatabase() {

	dsn := "root:krWXibAGjDyGxRvcAIuOTfgeOWsBIEuK@tcp(autorack.proxy.rlwy.net:44058)/railway?charset=utf8mb4&parseTime=True&loc=Local"

	database, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		log.Fatal("error", err)
	}

	fmt.Println("succes")
	DB = database
}

func main() {
	ConnectDatabase()
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{"message": "Hello, Golang with Gin!"})
	})
	r.Run(":8080")
}
