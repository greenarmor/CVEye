# 1st Stage: Build
FROM node:20 AS builder

WORKDIR /app

# Only copy package.json and package-lock.json to install deps first
COPY package.json package-lock.json ./

RUN npm install

# Copy rest of the code
COPY . .

RUN npm run build

# 2nd Stage: Production
FROM node:20-slim

WORKDIR /app

COPY --from=builder /app/.next/ .next/
COPY --from=builder /app/public/ public/
COPY --from=builder /app/package.json package.json

RUN npm install --only=production

EXPOSE 3000

CMD ["npm", "run", "start"]

