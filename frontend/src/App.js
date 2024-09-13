import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <main>
        <LateralBar />
      </main>
    </div>
  );
}

const LateralBar = () => {
  return (
    <div className="containerLeft">
      <div className='container-perfil'>
        <div className="icon-perfil">
          
        </div>
        <div className="name-perfil">Olá,</div>
      </div>

      <div className='container-options'>
        <div className="options">
          <div className="icon-options">
            
          </div>
          <div className="text-options">Início</div>
        </div>

        <div className="options">
          <div className="icon-options">
            
          </div>
          <div className="text-options">Configurações</div>
        </div>

        <div className="separator-line"></div>

        <div className="options">
          <div className="icon-options">
            
          </div>
          <div className="text-options">Notificações</div>
        </div>

        <div className="separator-line line-bottom"></div>

        
          <div className="options sair">
            <div className="icon-options">
              
            </div>
            <div className="text-options">Sair</div>
          </div>
        

        <div className="direitos bottom">
          Todos os direitos reservados ©
        </div>
      </div>
    </div>
  );
};

export default App;
