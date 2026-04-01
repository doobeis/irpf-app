@echo off
echo ==========================================================
echo Sincronizando o IRPF App (GPS Declaracao) com o GitHub...
echo ==========================================================
echo.
echo Aviso: Uma janela do GitHub vai abrir pedindo seu login se
echo voce ainda nao estiver conectado no Git!
echo.
cd ..
git push origin main
echo.
echo Prontinho! O comando de push acabou. Pode fechar essa janela.
pause
