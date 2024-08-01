# Use an official node image as the base image
FROM node:18-alpine AS build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Set the environment variable for the backend URL
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=${REACT_APP_API_URL}

# Build the React application
RUN npm run build

# Use an official nginx image to serve the application
FROM nginx:alpine

# Copy the build output from the previous stage to the nginx html directory
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8880
EXPOSE 8880

# Start nginx
CMD ["nginx", "-g", "daemon off;"]