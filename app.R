# Load required libraries
if (!require('shiny')) install.packages('shiny')
if (!require('ggplot2')) install.packages('ggplot2')
if (!require('dplyr')) install.packages('dplyr')
if (!require('DT')) install.packages('DT')
if (!require('shinythemes')) install.packages('shinythemes')

library(shiny)
library(ggplot2)
library(dplyr)
library(DT)
library(shinythemes)

# Load data set
data <- read.csv('cleaned_data.csv')

# Define UI
ui <- fluidPage(
  theme = shinytheme('cerulean'),
  titlePanel('Interactive Data Dashboard'),
  sidebarLayout(
    sidebarPanel(
      selectInput('product_category', 'Select Product Category:',
                  choices = unique(data$Product_Category),
                  multiple = TRUE),
      sliderInput('profitRange', 'Select Profit Range:',
                  min = min(data$Profit),
                  max = max(data$Profit),
                  value = c(min(data$Profit), max(data$Profit))),
      selectInput("plot_type", "Select Plot Type:",
                  choices = c("Line Plot", "Bar Chart", "Scatter Plot")),
      selectInput("x_var", "Select X-Axis Variable:",
                  choices = colnames(data), selected = "Date"),
      selectInput("y_var", "Select Y-Axis Variable:",
                  choices = colnames(data), selected = "Profit"),
      downloadButton("download_data", "Download Filtered Data")
    ),
    mainPanel(
      tabsetPanel(
        tabPanel("Plot", plotOutput("dynamicPlot")),
        tabPanel("Data Table", DTOutput("dataTable"))
      )
    )
  )
)

# Define Server
server <- function(input, output) {
  # Reactive filtering based on inputs
  filtered_data <- reactive({
    req(input$product_category)
    data %>%
      filter(Product_Category %in% input$product_category,
             Profit >= input$profitRange[1],
             Profit <= input$profitRange[2])
  })
  
  # Render dynamic plot
  output$dynamicPlot <- renderPlot({
    req(input$x_var, input$y_var)
    plot_data <- filtered_data()
    plot <- ggplot(plot_data, aes_string(x = input$x_var, y = input$y_var))
    
    if (input$plot_type == "Line Plot") {
      plot <- plot + geom_line(color = "blue")
    } else if (input$plot_type == "Bar Chart") {
      plot <- plot + geom_bar(aes_string(x = input$x_var), stat = "identity", fill = "blue")
    } else if (input$plot_type == "Scatter Plot") {
      plot <- plot + geom_point(color = "blue", size = 3)
    }
    
    plot + labs(title = paste(input$plot_type, "of", input$y_var, "vs", input$x_var),
                x = input$x_var,
                y = input$y_var) +
      theme_minimal()
  })
  
  # Render interactive data table
  output$dataTable <- renderDT({
    datatable(filtered_data(), options = list(pageLength = 10, scrollX = TRUE))
  })
  
  # Download filtered data
  output$download_data <- downloadHandler(
    filename = function() {
      paste("filtered_data-", Sys.Date(), ".csv", sep = "")
    },
    content = function(file) {
      write.csv(filtered_data(), file, row.names = FALSE)
    }
  )
}

# Run the app
if (interactive()) {
  shinyApp(ui = ui, server = server)
}
