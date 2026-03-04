class Object
  def tainted?
    false
  end

  def untaint
    self
  end

  def taint
    self
  end
end
