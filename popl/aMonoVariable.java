public interface aMonoVariable<T>{
	private T instance
	public void becomes(T val){
		if(unocupied(instance)){
			instance = val;
			this.notify();
		}else{
			this.wait();
		}
	}

	public T consume(){
		if(unocupied){
			this.wait();
		}else{
			this.notify();
			return instance;
		}
	}
}
