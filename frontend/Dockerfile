# Node.js 이미지를 기반으로 사용
FROM node:18-alpine

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY package.json package-lock.json ./

# 의존성 설치
RUN npm install

# 프로젝트 파일 복사
COPY . .

# Next.js 애플리케이션 빌드
RUN npm run build

# 애플리케이션 실행
CMD ["npm", "start"]
