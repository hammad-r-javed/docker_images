FROM arm64v8/haskell

RUN apt-get -y update &&\
    apt-get -y install neovim

RUN mkdir /root/.config && mkdir /root/.config/nvim

RUN git clone https://github.com/hammad-r-javed/nvim_init.git &&\
    cp nvim_init/init.vim /root/.config/nvim/init.vim &&\
    rm -rf nvim_init

CMD ["ghci"]
